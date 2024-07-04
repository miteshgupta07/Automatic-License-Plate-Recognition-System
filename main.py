from ultralytics import YOLO
import cv2
from sort.sort import *
import numpy as np
from util import get_car

# Load Model
vehicle_tracker=Sort()

vehicle_detection_model=YOLO('yolov8n.pt')
license_plate_detector=YOLO('License_Plate_Detector.pt')

# Load Video
cap=cv2.VideoCapture("E:\Data Science\Projects\Sample.mp4")

vehicle_list=[2,3,5,7]

while True:
    # if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
    #         cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    # Read Frames
    success,frame=cap.read()
    if not success:
        break
    
    # Detect Vehicles
    detections=vehicle_detection_model(frame)[0]
    detect=[]
    for detection in detections.boxes.data.tolist():
        x1,y1,x2,y2,score,class_id=detection
        if int(class_id) in vehicle_list:
            detect.append([x1,y1,x2,y2,score])

    # Track Vehicles
    track_ids=vehicle_tracker.update(np.asarray(detect))

    # Detect License Plates
    license_plates=license_plate_detector(frame)[0]
    for license_plate in license_plates.boxes.data.tolist():
            x1,y1,x2,y2,score,class_id=license_plate

            # Assign License Plate To Car
            x_car1,y_car1,x_car2,y_car2,car_id=get_car(license_plate,track_ids)

            # Crop License Plate
            license_plate_crop=frame[int(y1):int(y2), int(x1):int(x2)]

            # Process License PLate
            gray_license_plate=cv2.cvtColor(license_plate_crop,cv2.COLOR_BGR2GRAY)
            _,threshold_license_plate=cv2.threshold(gray_license_plate,64,255,cv2.THRESH_BINARY_INV)