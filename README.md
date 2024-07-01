## Prerequisites

### 1. Download Required Files

- Download YOLOv8 model:
  - [YOLOv8n](https://github.com/ultralytics/assets/releases/download/v8.2.0/yolov8n.pt)
  - [YOLOv8s](https://github.com/ultralytics/assets/releases/download/v8.2.0/yolov8s.pt)
  - [YOLOv8m](https://github.com/ultralytics/assets/releases/download/v8.2.0/yolov8m.pt)


- Download a test video
```commandline
sudo snap install yt-dlp
yt-dlp https://youtu.be/ORrrKXGx2SE?si=30vqNKJDTSy8bEHO -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4" -o ./resource/test.mp4
```


### 2. Install Required Libraries

Run the following command to install the necessary libraries:

```commandline
pip install ultralytics opencv-python numpy torch
```

### 3. Run
1. Inference using yolov8 only.
```commandline
python ./inference/yolov8.py
```

2. Inference using yolov8 + sort.
```commandline
python ./inference/yolov8_sort.py
```

### 4. Result
You can see the inference results during execution or check them in the result folder.

![yolov8_result](https://github.com/dev-jinwoohong/human-detection/assets/70004933/378a4883-fe81-4571-9bf9-33f019eac567)

