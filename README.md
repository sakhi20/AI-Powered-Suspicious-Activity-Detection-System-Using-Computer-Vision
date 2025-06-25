# 🔍 Suspicious Activity Detection System (YOLOv8)

A real-time surveillance system using **YOLOv8** to detect suspicious objects like **knives** and **masks**, with optional **email alerts**.

---

## 🚀 Features

- ✅ Custom-trained YOLOv8 model
- 🎥 Live video detection via webcam
- 📨 Email alerts for knife/mask detection
- 📏 Filters based on confidence and bounding box size
- 🖼 Bounding box visualization
---

## ⚙️ Usage

### 🔧 Train the Model
```bash
python training.py
```

### 🎯 Run Live Detection
```bash
python main.py
```

---

## 📧 Setup Email Alerts

Edit in `main.py`:
```python
sender_email = "your_email@gmail.com"
receiver_email = "to_email@gmail.com"
password = "your_app_password"
```

---

## 📦 Requirements

```bash
pip install ultralytics opencv-python
```

---

## 🏷️ Classes

| ID | Object |
|----|--------|
| 0  | Knife  |
| 1  | Person |
| 2  | Mask   |

---

## 🧠 Credits

- Sakhi Patel
- Prerana Somani
- Sakshi Patel

