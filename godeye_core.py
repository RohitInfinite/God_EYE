import cv2
import time

from core.detection import detect_objects
from core.depth import get_depth_map
from core.navigation import get_direction, generate_sentence, IMPORTANT_OBJECTS
from core.speech import speak

running = False
previous_distance = {}
detected_objects = 0

def main():

    global running
    running = True

    cap = cv2.VideoCapture(0)

    last_spoken = time.time()

    while running:

        ret, frame = cap.read()

        if not ret:
            break

        frame = cv2.flip(frame, 1)

        frame_width = frame.shape[1]

        depth_map = get_depth_map(frame)

        detections = detect_objects(frame)

        spoken_text = []

        for obj in detections:
            global detected_objects
            detected_objects = len(detections)

            label = obj["label"]

            if label not in IMPORTANT_OBJECTS:
                continue

            x1, y1, x2, y2 = obj["box"]
            cx, cy = obj["center"]

            depth_value = depth_map[cy, cx]

            distance = int(depth_value / 100)

            direction = get_direction(cx, frame_width)

            sentence = generate_sentence(label, direction, distance)

            prev = previous_distance.get(label)

            if prev is not None and distance < prev - 1:
                sentence = f"Warning! {label} approaching"

            previous_distance[label] = distance

            spoken_text.append((label, sentence))

            cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0),2)

            cv2.putText(
                frame,
                sentence,
                (x1, y1-10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0,255,0),
                2
            )

        current_time = time.time()

        if current_time - last_spoken > 3:

            if spoken_text:

                message = spoken_text[0][1]

            else:

                message = "Path seems clear"

            speak(message)

            last_spoken = current_time

        cv2.imshow("GOD-EYE", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            running = False

    cap.release()
    cv2.destroyAllWindows()