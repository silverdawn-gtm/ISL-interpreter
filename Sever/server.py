from fastapi import FastAPI, File, UploadFile
import tensorflow as tf
import numpy as np
import cv2
import mediapipe as mp
from io import BytesIO
from PIL import Image
import gdown
import os
from starlette.concurrency import run_in_threadpool

app = FastAPI()

# Model Download & Load
MODEL_PATH = "model.h5"
DRIVE_FILE_ID = "1abcDXYZ123456789"  # Replace with your Google Drive file ID

def download_model():
    if not os.path.exists(MODEL_PATH) or os.path.getsize(MODEL_PATH) == 0:
        print("Downloading model from Google Drive...")
        url = f"https://drive.google.com/uc?id={DRIVE_FILE_ID}"
        gdown.download(url, MODEL_PATH, quiet=False)

download_model()  # Ensure model is downloaded before loading
model = tf.keras.models.load_model(MODEL_PATH)

# Initialize MediaPipe Hand Landmark Detector
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=True, max_num_hands=1)

def extract_landmarks(image):
    """Extracts hand landmarks from an image using MediaPipe"""
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            return np.array([[lm.x, lm.y, lm.z] for lm in hand_landmarks.landmark]).flatten()

    return np.zeros(63)  # Return an empty array instead of None

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(BytesIO(contents)).convert("RGB")
    image = np.array(image)

    landmarks = extract_landmarks(image)
    if landmarks is None:
        return {"error": "No hand detected"}

    landmarks_tensor = np.expand_dims(landmarks, axis=0)  # Reshape for model input

    # Run model.predict() in a separate thread
    output = await run_in_threadpool(model.predict, landmarks_tensor)
    prediction = np.argmax(output, axis=1)[0]  # Get class label

    return {"prediction": int(prediction)}

# Run locally: uvicorn server:app --host 0.0.0.0 --port 8000
