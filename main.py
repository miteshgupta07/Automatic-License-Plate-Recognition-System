from ultralytics import YOLO
import cv2
from sort.sort import *
import numpy as np

vehicle_tracker=Sort()

vehicle_detection_model=YOLO('yolov8n.pt')
license_plate_detector=YOLO('License_Plate_Detector.pt')

cap=cv2.VideoCapture("Sample.mp4")

vehicle_list=[2,3,5,7]

while True:
    # if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
    #         cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    success,frame=cap.read()
    if not success:
        break

    detections=vehicle_detection_model(frame)[0]
    detect=[]
    for detection in detections.boxes.data.tolist():
        x1,y1,x2,y2,score,class_id=detection
        if int(class_id) in vehicle_list:
            detect.append([x1,y1,x2,y2,score])

    track_ids=vehicle_tracker.update(np.asarray(detect))
    license_plates=license_plate_detector(frame)[0]
    for license_plate in license_plates.boxes.data.tolist():
            x1,y1,x2,y2,score,class_id=license_plate