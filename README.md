# AI-Powered Suspicious Activity Detection System Using Computer Vision

![Precision](https://img.shields.io/badge/Precision-87%25-brightgreen) ![Recall](https://img.shields.io/badge/Recall-83%25-brightgreen) ![mAP@0.5](https://img.shields.io/badge/mAP%400.5-0.85-brightgreen) ![FPS](https://img.shields.io/badge/FPS-~25-blue) ![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-green)

## Overview

A YOLOv8 transfer learning system fine-tuned to detect knives near people in video feeds. The model detects `knife_weapon` and `person` instances in each frame; when a weapon bounding box centroid falls within 50 pixels of a person bounding box centroid, the frame is flagged as suspicious activity and bounding boxes turn red.

Trained via transfer learning on a custom Kaggle dataset with 100 epochs, frozen backbone (100 layers), and 320px input resolution. Achieves 87% precision, 83% recall, and 0.85 mAP@0.5 at ~25 FPS.

---

## 📁 Project Structure

```
├── main.py                 # Inference: webcam/video detection + proximity logic
├── training.py             # YOLOv8 fine-tuning script
├── my_yolov8_model.pt      # Trained model weights (custom knife+person)
├── Project Report.pdf      # Full academic report with methodology
└── README.md
```

---

## How It Works

1. **Object detection** — YOLOv8 detects all instances of `knife_weapon` (class 0) and `person` (class 1) in each video frame
2. **Proximity analysis** — For each weapon detection, the Euclidean distance from the weapon centroid to every person bounding box center is computed
3. **Suspicious activity flag** — If any weapon-to-person distance falls below the 50px threshold, the frame is flagged as suspicious
4. **Visual output** — Bounding boxes drawn green (normal) or red (suspicious); alert message displayed on frame

### Training Configuration

| Parameter | Value |
|-----------|-------|
| Epochs | 100 |
| Image size | 320 px |
| Batch size | 8 |
| Frozen layers | 100 (backbone) |
| Confidence threshold | 0.25 |
| IoU threshold | 0.5 |

---

## 📊 Performance Metrics

| Metric | Value |
|--------|-------|
| Precision | 0.87 |
| Recall | 0.83 |
| mAP@0.5 | 0.85 |
| Frame Rate | ~25 FPS |

---

## Usage

### Install dependencies

```bash
pip install ultralytics opencv-python numpy
```

### Run inference on webcam

```bash
python main.py
# Opens default webcam (source=0); press Q to quit
```

### Run inference on a video file

Edit `main.py` and set `source` to your video file path, then run:

```bash
python main.py
```

### Fine-tune on a new dataset

Edit `training.py` to point to your `data.yaml`, then:

```bash
python training.py
```

---

## ⚠️ Responsible AI Notice

This system was developed for academic research purposes. Real-world deployment of automated surveillance systems raises important ethical considerations including:

- **Privacy**: Video surveillance requires informed consent and legal compliance (GDPR, CCPA, etc.)
- **Bias**: Weapon detection models may perform differently across demographic groups and lighting conditions
- **False positives**: Any production deployment must include human review workflows — automated alerts alone are insufficient
- **Scope**: This model detects knives only; it should not be used for general threat assessment

---

## Academic Context

**Undergraduate Final Year Project**
Pandit Deendayal Energy University (PDEU), Gandhinagar
Department of Information and Communication Technology, School of Technology
Academic Year 2024–2025

| Role | Name | Enrollment |
|------|------|-----------|
| Team Member | Sakshi Patel | 21BIT163 |
| Team Member | Prerana Somani | 21BIT180 |
| Team Member | Sakhi Patel | 21BIT182 |
| Faculty Guide | Dr. Paawan Sharma | Associate Professor, ICT |

Full methodology, literature review, and experimental results are documented in [Project Report.pdf](./Project%20Report.pdf).

---

## Acknowledgments

- [Ultralytics](https://github.com/ultralytics/ultralytics) for the YOLOv8 framework
- Kaggle for the knife detection dataset used in fine-tuning
- OpenCV community for computer vision tooling
