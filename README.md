# GOD-EYE

## AI Powered Assistive Navigation System for the Visually Impaired

**GOD-EYE** is a real-time AI-based assistive navigation system designed to help visually impaired individuals understand their surroundings using computer vision and voice guidance.

The system detects objects, estimates their distance and direction, and provides audio feedback to guide the user safely.

---
# Image of GUI
![GOD-EYE GUI](GOD-EYE%20Image.png)
---
# Demo Video
[Download / Watch Demo](GoD-EYE%20DEMO.mp4)
---
# Features

* Real-time object detection using **YOLOv8**
* Depth estimation using **MiDaS model**
* Direction awareness (**Left / Center / Right**)
* Distance estimation of obstacles
* Voice guidance for navigation
* Voice assistant activation (**"Hey God"**)
* Stop navigation voice command
* Futuristic AI dashboard interface
* Real-time camera processing

---

# Tech Stack

### Programming Language

* Python

### Computer Vision

* OpenCV
* YOLOv8 (Ultralytics)

### Depth Estimation

* MiDaS (Intel-ISL)

### AI Framework

* PyTorch

### Speech Processing

* SpeechRecognition
* pyttsx3

### GUI

* Tkinter

---

# Project Structure

```
GOD-EYE/
│
├── godeye_app.py          # GUI Application
├── godeye_core.py         # Main system pipeline
├── voice_activation.py    # Voice command handler
│
├── core/
│   ├── detection.py       # Object detection
│   ├── depth.py           # Depth estimation
│   ├── navigation.py      # Navigation logic
│   ├── speech.py          # Voice output system
│
├── Models/
│   └── yolov8n.pt         # YOLO model
│
├── requirements.txt
├── README.md
```

---

# Installation

Clone the repository:

```bash
git clone https://github.com/RohitInfinite/God_EYE.git
cd God_EYE
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the system:

```bash
python godeye_app.py
```

---

# Voice Commands

| Command             | Action           |
| ------------------- | ---------------- |
| **Hey God**         | Start Navigation |
| **Stop Navigation** | Stop System      |

---

# Use Case

This system can assist visually impaired users by providing real-time environmental awareness and safe navigation using AI-powered vision and voice feedback.

---

# Author

**Rohit Khandelwal**
