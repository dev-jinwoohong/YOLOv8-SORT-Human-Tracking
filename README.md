
![facebook_cover_photo_2](https://github.com/dev-jinwoohong/YOLOv8-SORT-Human-Tracking/assets/70004933/e52fd191-57f8-4f35-9a7b-fc792e3957e3)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
![Python](https://img.shields.io/badge/python-v3.8-blue.svg)
[![GitHub Issues](https://img.shields.io/github/issues/dev-jinwoohong/YOLOv8-SORT-Human-Tracking.svg)](https://github.com/dev-jinwoohong/YOLOv8-SORT-Human-Tracking/issues)
![Contributions welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)
[![License](https://img.shields.io/badge/license-GNU-yellow.svg)](https://opensource.org/licenses/GNU)


## Prerequisites

### 1. Download Required Files

- Download YOLOv8 model put it in the `resource` folder:
  - [YOLOv8n](https://github.com/ultralytics/assets/releases/download/v8.2.0/yolov8n.pt)
  - [YOLOv8s](https://github.com/ultralytics/assets/releases/download/v8.2.0/yolov8s.pt)
  - [YOLOv8m](https://github.com/ultralytics/assets/releases/download/v8.2.0/yolov8m.pt)


- Download a test video
```commandline
sudo snap install yt-dlp
yt-dlp https://youtu.be/2SATljljXCY?si=y8Lbldme2RhQADCP -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4" --download-sections "*00:00:00-00:00:17" -o ./resource/sample.mp4
```


### 2. Install Required Libraries

Run the following command to install the necessary libraries:
```commandline
pip install -r requirements.txt
```

### 3. Run
1. Inference using yolov8 only.
```commandline
python yolov8.py
```

2. Inference using yolov8 + sort.
```commandline
python yolov8_sort.py
```

### 4. Result
You can see the inference results during execution or check them in the result folder.

- YOLOv8 Result

![yolov8_result.gif](result/yolov8_result.gif)

- YOLOv8 + SORT Result

![yolov8_result.gif](result/yolov8_sort_result.gif)

