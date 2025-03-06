# Real-Time Indian Sign Language (ISL) Recognition System

## Overview
This project is a **Real-Time Indian Sign Language (ISL) Recognition System** that can recognize hand gestures and translate them into text and speech. It supports both **offline and online recognition** modes, ensuring accessibility even without an internet connection.

## Features
- **Real-Time Hand Gesture Recognition** using a camera.
- **Hand Tracking & Feature Extraction** powered by **MediaPipe**.
- **Offline Mode** using **MobileViT + GRU (TFLite)** for on-device processing.
- **Online Mode** utilizing a **Cloud-Based Transformer Model** for improved accuracy.
- **Hybrid Switching** based on network availability.
- **Gesture Processing Pipeline** to convert keypoints into features and classify them.
- **Text & Speech Output** using Flutter TTS.
- **Flutter-based User Interface** for seamless interaction.

## Tech Stack
### **Frontend (Flutter App)**
- **Flutter** (Dart) for cross-platform mobile development
- **Camera Plugin** for video input
- **TFLite Plugin** for offline ML inference
- **Text-to-Speech (TTS)** for audio output

### **Machine Learning Model**
- **MediaPipe** for hand landmark detection
- **MobileViT + GRU** for lightweight on-device recognition
- **Transformer Model** for cloud-based recognition
- **TensorFlow Lite (TFLite)** for optimized inference

### **Backend (Cloud-Based System)**
- **FastAPI / Flask** for serving the Transformer model
- **AWS / GCP** for cloud hosting
- **Database (optional)** for storing custom gestures

## Installation & Setup
### **1. Clone the Repository**
```sh
 git clone https://github.com/your-repo/ISL-Recognition.git
 cd ISL-Recognition
```

### **2. Install Flutter Dependencies**
```sh
 flutter pub get
```

### **3. Run the Flutter App**
```sh
 flutter run
```

### **4. Deploy Backend (For Cloud-Based Model)**
- Install Python dependencies:
  ```sh
  pip install -r requirements.txt
  ```
- Run FastAPI server:
  ```sh
  uvicorn main:app --host 0.0.0.0 --port 8000
  ```

## Usage
1. Open the app and grant camera permissions.
2. Start capturing hand gestures.
3. The system will detect, process, and classify the sign.
4. The recognized sign will be displayed as text and spoken aloud.
5. Toggle between offline and online recognition based on network availability.

## Future Enhancements
- Add support for sentence-level recognition.
- Improve model accuracy with a larger dataset.
- Implement a custom gesture-learning feature.
- Support multiple sign languages beyond ISL.

## Contributors


## License
This project is licensed under the **MIT License**.
