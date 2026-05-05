import cv2
from ultralytics import YOLO

# Model load karen
model = YOLO('yolov8s.pt') 

# Webcam open karen
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    # Objects detect karen
    results = model.track(frame, persist=True)

    # Sirf un objects ko dikhayen jo 'person' nahi hain
    # YOLO mein class 0 'person' hoti hai
    for result in results:
        # Filter: Sirf wo boxes rakhen jin ki class ID 0 (person) nahi hai
        result.boxes = result.boxes[result.boxes.cls != 0]

    # Annotated frame banayen (Ab is mein insaan par box nahi banega)
    annotated_frame = results[0].plot()

    # Output display karen
    cv2.imshow("CodeAlpha Task 4 - No Person Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()