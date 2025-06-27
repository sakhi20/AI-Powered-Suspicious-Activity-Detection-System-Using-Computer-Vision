# AI-Powered Suspicious Activity Detection System Using Computer Vision

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://python.org)
[![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-green.svg)](https://github.com/ultralytics/ultralytics)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.0%2B-red.svg)](https://opencv.org)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 🎯 Overview

An intelligent surveillance system that leverages cutting-edge computer vision and machine learning techniques to automatically detect suspicious activities in real-time video feeds. The system uses YOLOv8 for object detection and implements proximity-based analysis to identify potential threats, particularly focusing on weapon detection near individuals.

## 🚀 Features

- **Real-time Detection**: Processes video feeds at ~25 FPS for immediate threat identification
- **High Accuracy**: Achieves 87% precision and 83% recall with 0.85 mAP@0.5
- **Intelligent Analysis**: Context-aware detection using proximity-based suspicious activity rules
- **Flexible Input**: Supports both live webcam feeds and pre-recorded video files
- **Scalable Architecture**: Modular design for easy deployment across various environments
- **Visual Feedback**: Real-time bounding box visualization with suspicious activity alerts

## 🛠️ Technical Stack

- **Deep Learning Framework**: YOLOv8 (Ultralytics)
- **Computer Vision**: OpenCV
- **Programming Language**: Python 3.8+
- **Data Processing**: NumPy, Pandas
- **Model Training**: Transfer Learning with pre-trained YOLOv8

## 📋 Prerequisites

```bash
Python 3.8 or higher
CUDA-compatible GPU (recommended for real-time processing)
Webcam or video files for testing
```

## 📁 Project Structure

```
suspicious-activity-detection/
│
├── models/
│   ├── my_yolov8_model.pt      # Trained custom model
│   └── yolov8n.pt              # Base YOLOv8 model
│
├── data/
│   ├── train/                  # Training dataset
│   ├── val/                    # Validation dataset
│   └── data.yaml               # Dataset configuration
│
├── src/
│   ├── train.py                # Model training script
│   ├── detect.py               # Detection and inference
│   └── utils.py                # Utility functions
│
├── outputs/                    # Detection results
├── requirements.txt            # Project dependencies
└── README.md                   # Project documentation
```

## 🚀 Quick Start

### 1. Training the Model
Run the training script with the prepared dataset to create a custom model for suspicious activity detection.

### 2. Running Detection

The system supports multiple input sources:
- **Webcam feed**: Real-time detection from connected camera
- **Video file**: Process pre-recorded surveillance footage
- **Image**: Analyze static images for suspicious objects

## ⚙️ Configuration

### Training Parameters
- **Epochs**: 100 training iterations
- **Image Size**: 320 pixels for optimal performance
- **Batch Size**: 8 for memory efficiency
- **Confidence Threshold**: 0.25 for filtering weak detections
- **IoU Threshold**: 0.5 for Non-Max Suppression
- **Freeze Layers**: 100 layers frozen for transfer learning

### Detection Parameters
- **Proximity Threshold**: 50 pixels for suspicious activity detection
- **Confidence Threshold**: 0.25 minimum confidence for valid detections
- **Detection Classes**: knife_weapon and person

## 📊 Performance Metrics

| Metric | Value |
|--------|-------|
| Precision | 0.87 |
| Recall | 0.83 |
| mAP@0.5 | 0.85 |
| Frame Rate | ~25 FPS |

## 🎯 Detection Classes

The system is trained to detect:
- **knife_weapon** (Class ID: 0)
- **person** (Class ID: 1)

Suspicious activity is flagged when a weapon is detected within the proximity threshold of a person.

## 📈 System Workflow

### Detection Process
1. **Video Input**: System captures frames from webcam or video file
2. **Object Detection**: YOLOv8 model identifies weapons and persons in each frame
3. **Proximity Analysis**: Calculates distance between detected objects
4. **Activity Classification**: Flags suspicious activities based on proximity rules
5. **Alert Generation**: Provides real-time notifications for security personnel
6. **Visual Output**: Displays detection results with bounding boxes and labels

## 🔬 Research and Development

This project addresses key challenges in automated surveillance:

### Research Gaps Addressed
- Manual surveillance dependency
- Limited real-time detection capabilities
- High false alarm rates
- Inadequate scalability
- Lack of context-aware detection

### Novel Contributions
- Proximity-based suspicious activity detection
- Real-time processing with high accuracy
- Transfer learning approach for custom object detection
- Scalable architecture for various deployment scenarios

## 🏗️ Future Enhancements

### Planned Features
- [ ] Multi-object detection (firearms, suspicious bags)
- [ ] Advanced behavior analysis using temporal patterns
- [ ] IoT integration for automated response systems
- [ ] Edge computing deployment
- [ ] Cloud-based monitoring dashboard
- [ ] Privacy-preserving techniques

### Research Directions
- Ensemble models for reduced false positives
- Dynamic threshold adaptation
- Audio analysis integration
- Bias mitigation techniques

## 👥 Authors

- **Sakshi Patel** - 21BIT163
- **Prerana Somani** - 21BIT180  
- **Sakhi Patel** - 21BIT182

**Under the Guidance of:**
- **Dr. Paawan Sharma** - Associate Professor, Department of ICT, PDEU

## 🏫 Institution

Department of Information and Communication Technology  
School of Technology  
Pandit Deendayal Energy University, Gandhinagar  
AY 2024-2025

## 🙏 Acknowledgments

- **Kaggle** for providing valuable datasets
- **Ultralytics** for the YOLOv8 framework
- **OpenCV** community for computer vision tools
- **Open-source community** for continuous support and resources

## 📚 References

For detailed research background and citations, please refer to our [project report]([Project Report.pdf](https://github.com/sakhi20/AI-Powered-Suspicious-Activity-Detection-System-Using-Computer-Vision/blob/446183aa47b7a8d14c7b8714b871de635af87b5d/Project%20Report.pdf)).

---

⭐ **Star this repository if you find it helpful!**

**Made with ❤️ for public safety and security**
