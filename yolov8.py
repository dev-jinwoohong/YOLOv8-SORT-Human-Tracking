from ultralytics import YOLO
import cv2
import os
import random
import time


def get_random_color():
    return [random.randint(0, 255) for _ in range(3)]


model = YOLO("resource/yolov8.pt")
video = cv2.VideoCapture('resource/sample.mp4')
fps = video.get(cv2.CAP_PROP_FPS)
frame_time = 1 / fps
color_dict = {}

downscale = 4

width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH)) // downscale
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT)) // downscale

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
os.makedirs('result', exist_ok=True)
out = cv2.VideoWriter('result/yolov8_result.mp4', fourcc, fps, (width, height))

while True:
    start_time = time.time()

    ret, frame = video.read()
    if not ret:
        break

    frame = cv2.resize(frame, (width, height))

    results = model(frame)
    height, width = frame.shape[:2]

    for result in results:
        for box in result.boxes:
            if int(box.cls.item()) != 0:
                continue
            lx, ly, rx, ry = (int(coord * dim) for coord, dim in zip(box.xyxyn[0], [width, height] * 2))

            obj_id = int(box.id.item()) if box.id is not None else random.randint(0, 10000)

            if obj_id not in color_dict:
                color_dict[obj_id] = get_random_color()
            color = color_dict[obj_id]

            cv2.rectangle(frame, (lx, ly), (rx, ry), color, 2)

            label = f"{obj_id}"

            (label_width, label_height), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)

            label_x = lx
            label_y = ly - 10 if ly - 10 > label_height else ly + 10

            cv2.rectangle(frame, (label_x, label_y - label_height), (label_x + label_width, label_y + label_height),
                          color, cv2.FILLED)
            cv2.putText(frame, label, (label_x, label_y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)

    out.write(frame)

    cv2.imshow("output", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    processing_time = time.time() - start_time

    wait_time = max(1, int((frame_time - processing_time) * 1000))
    cv2.waitKey(wait_time)

video.release()
out.release()
cv2.destroyAllWindows()
