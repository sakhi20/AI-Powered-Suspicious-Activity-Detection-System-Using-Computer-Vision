import cv2
from ultralytics import YOLO
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Load the trained YOLOv8 model
model = YOLO('C:/Users/PRERANA/Desktop/PDEU/minor project/my_yolov8_model.pt')  # Update with your model path

# Function to send email notification
def send_email_notification(alert_type):
    sender_email = "sakhi.pict21@sot.pdpu.ac.in"
    receiver_email = "prerana.sict21@sot.pdpu.ac.in"
    password = "opbrrmdlgaihvnmt"  # App Password

    subject = f"Suspicious Activity Detected: {alert_type}!"
    body = f"Alert: Suspicious activity detected involving a {alert_type}."

    # Create the email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Set up the SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)  # SMTP server for Gmail
        server.starttls()  # Upgrade to a secure encrypted SSL/TLS connection
        server.login(sender_email, password)  # Login using your email and app password
        server.send_message(msg)  # Send the email
        print(f"Email notification sent: {alert_type} detected!")
    except Exception as e:
        print(f"Failed to send email: {e}")
    finally:
        server.quit()  # Close the SMTP server connection

# Initialize webcam
cap = cv2.VideoCapture(0)  # 0 for webcam

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run YOLO model inference on the frame
    results = model(frame)

    knife_detected = False
    mask_detected = False

    # Process results to check for detections and probabilities
    detections = results[0].boxes  # Access the first result's boxes

    for detection in detections:  # Each detection is an instance of a Box object
        class_id = int(detection.cls[0])  # Get the class ID
        confidence = detection.conf[0]  # Get the confidence score for this detection
        box = detection.xyxy[0]  # Get the bounding box (x_min, y_min, x_max, y_max)
        box_width = box[2] - box[0]
        box_height = box[3] - box[1]

        # Debugging information
        print(f"Detected Class: {class_id}, Confidence: {confidence}, Box Size: {box_width * box_height}")

        if confidence > 0.95:  # Only consider detections with high confidence
            # Filter based on bounding box size for masks
            if class_id == 2:  # Assuming 'mask' class ID is 2
                if box_width * box_height < 5000:  # Adjust threshold for small objects
                    mask_detected = True
                else:
                    print("Large bounding box ignored for mask")
            elif class_id == 0:  # Assuming 'knife_weapon' class ID is 0
                knife_detected = True

    # Send email notification for detected items
    if knife_detected:
        send_email_notification("Knife")
    if mask_detected:
        send_email_notification("Mask")

    # Render results and show the frame
    cv2.imshow('Frame', results[0].plot())  # Show detections
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
        break

cap.release()
cv2.destroyAllWindows()
