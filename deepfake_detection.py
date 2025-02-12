import torch
import torchvision.transforms as transforms
import cv2
import numpy as np

# Load deepfake detection model (dummy model for now)
def load_model():
    model = torch.nn.Linear(10, 1)  # Placeholder for actual model
    model.eval()
    return model

model = load_model()

def preprocess_frame(frame):
    transform = transforms.Compose([transforms.ToTensor()])
    return transform(frame).unsqueeze(0)

def analyze_video(video_path):
    cap = cv2.VideoCapture(video_path)
    fake_score = 0
    frame_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame_count += 1
        input_tensor = preprocess_frame(frame)
        with torch.no_grad():
            prediction = model(input_tensor)
            fake_score += prediction.item()

    cap.release()
    
    confidence = (fake_score / frame_count) * 100 if frame_count else 0
    return ("Fake" if confidence > 50 else "Real"), confidence
