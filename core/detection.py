from ultralytics import YOLO

model = YOLO("models/yolov8n.pt")


def detect_objects(frame):

    results = model(frame)

    detections = []

    for r in results:

        for box in r.boxes:

            if box.conf[0] < 0.5:
                continue

            x1, y1, x2, y2 = map(int, box.xyxy[0])

            cls = int(box.cls[0])

            label = model.names[cls]

            cx = int((x1 + x2) / 2)
            cy = int((y1 + y2) / 2)

            detections.append({
                "label": label,
                "box": (x1, y1, x2, y2),
                "center": (cx, cy)
            })

    return detections