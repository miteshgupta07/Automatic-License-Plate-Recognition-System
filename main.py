from ultralytics import YOLO
import cv2
from sort.sort import *
import numpy as np
from scipy.interpolate import interp1d
from util import get_car, read_license_plate, write_csv

results = {}

vehicle_tracker = Sort()

# load models
vehicle_detection_model = YOLO('yolov8n.pt')
license_plate_detector = YOLO('License_Plate_Detector.pt')

# load video
cap = cv2.VideoCapture('E:\\Data Science\\Projects\\Sample.mp4')

vehicle_list = [2, 3, 5, 7]

# read frames
frame_count = -1
success = True
while success:
    frame_count += 1
    success, frame = cap.read()
    if success:
        results[frame_count] = {}
        # detect vehicle_list
        detections = vehicle_detection_model(frame)[0]
        detections_ = []
        for detection in detections.boxes.data.tolist():
            x1, y1, x2, y2, score, class_id = detection
            if int(class_id) in vehicle_list:
                detections_.append([x1, y1, x2, y2, score])

        # track vehicle_list
        track_ids = vehicle_tracker.update(np.asarray(detections_))

        # detect license plates
        license_plates = license_plate_detector(frame)[0]
        for license_plate in license_plates.boxes.data.tolist():
            x1, y1, x2, y2, score, class_id = license_plate

            # assign license plate to car
            xcar1, ycar1, xcar2, ycar2, car_id = get_car(
                license_plate, track_ids)

            if car_id != -1:

                # crop license plate
                license_plate_crop = frame[int(
                    y1):int(y2), int(x1): int(x2), :]

                # process license plate
                license_plate_crop_gray = cv2.cvtColor(
                    license_plate_crop, cv2.COLOR_BGR2GRAY)
                _, license_plate_crop_thresh = cv2.threshold(
                    license_plate_crop_gray, 64, 255, cv2.THRESH_BINARY_INV)

                # read license plate number
                license_plate_text, license_plate_text_score = read_license_plate(
                    license_plate_crop_thresh)

                if license_plate_text is not None:
                    results[frame_count][car_id] = {'car': {'bbox': [xcar1, ycar1, xcar2, ycar2]},
                                                    'license_plate': {'bbox': [x1, y1, x2, y2],
                                                                      'text': license_plate_text,
                                                                      'bbox_score': score,
                                                                      'text_score': license_plate_text_score}}

# write results
write_csv(results, './test.csv')