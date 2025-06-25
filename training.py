from ultralytics import YOLO

# Load a pre-trained YOLOv8 model
model = YOLO(r'C:\Users\PRERANA\Desktop\PDEU\minor project\models\yolov8n.pt')

layers = model.model.model  # Access the model's layers

# Freeze the first 30 layers
for i, layer in enumerate(layers):
    if i < 30:  # Freeze the first 30 layers
        for param in layer.parameters():
            param.requires_grad = False

results = model.train(
    data = r'C:\Users\PRERANA\Desktop\PDEU\minor project\data.yaml',
    epochs=5,
    imgsz=320,  
    batch=8,   
    conf=0.25,  
    max_det=100,  
    iou=0.5,  
)

# Save the trained model in a relative path
model.save('./my_yolov8_model.pt')
