# Object Detection and Tracking - CodeAlpha Task 4

## Project Overview
This project is part of my Artificial Intelligence internship at **CodeAlpha**. It implements real-time object detection and tracking using the **YOLOv8** model and **OpenCV**. The system can identify various objects through a webcam or video file and assign unique tracking IDs to them.

## Features
*   **Real-time Detection:** High-speed object identification using YOLOv8.
*   **Object Tracking:** Assigns and maintains unique IDs for objects across frames.
*   **Privacy Filter:** The code is configured to filter/ignore specific classes (like 'person') to focus on object analysis.
*   **Live Output:** Displays annotated video frames with bounding boxes and labels.

## Installation & Setup
1. Clone this repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/CodeAlpha_ObjectDetection.git](https://github.com/YOUR_USERNAME/CodeAlpha_ObjectDetection.git)

  2.Install the required dependencies:
  ``bash
  pip install -r requirements.txt

 3.How to Run
Run the main script using Python:
```bash
python app.py
