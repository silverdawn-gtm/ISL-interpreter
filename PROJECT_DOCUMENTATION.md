# Project Documentation

## Overview
This is a **Sign Language Interpreter** application consisting of a Flutter mobile application (Android) and a Python Flask backend server. The system recognizes hand gestures and sign language using MediaPipe hand detection and TensorFlow/Keras deep learning models.

**Purpose:** Translate sign language gestures (both static and dynamic) into text/speech output.

## Project Structure

### Root Directories

#### `/android_app/test_123/` - Flutter Mobile Application
A Flutter-based Android application for sign language recognition:

**Key Directories:**
- `lib/` - Dart source code
  - `main.dart` - Application entry point (SignLanguageApp)
  - `screens/` - Screen components
    - `home_screen.dart` - Main home screen
  - `widgets/` - Reusable UI components
    - `camera_preview.dart` - Camera preview widget
    - `control_buttons.dart` - Control button widgets
    - `homepage.dart` - Homepage widget
    - `output_box.dart` - Output display widget
    - `progress_bar.dart` - Progress indicator widget
    - `settings_sheet.dart` - Settings UI component

- `android/` - Android-specific configuration and build files
  - `app/` - Main app module
  - `gradle/` - Gradle build system files
  - `build.gradle.kts` - Gradle build configuration

- `assets/` - Application assets
  - `app_icon.png` - Application icon

- `test/` - Test files
  - `widget_test.dart` - Widget tests

**Configuration Files:**
- `pubspec.yaml` - Flutter/Dart dependencies and project configuration
- `pubspec.lock` - Locked dependency versions
- `analysis_options.yaml` - Dart analysis configuration

**Dependencies:**
- `camera: ^0.10.5+5` - Camera access
- `http: ^1.3.0` - HTTP requests to backend
- `flutter_tts: ^3.8.3` - Text-to-speech output
- `provider: ^6.0.5` - State management
- `path_provider: ^2.1.1` - File system access

#### `/Server/flask_server/` - Python Backend Server
A Flask-based Python server for sign language recognition:

**Key Files:**
- `main.py` - Primary Flask application with `/predict` endpoint
  - Loads MobileViT landmarks model
  - Handles static image uploads
  - Extracts hand landmarks using MediaPipe
  - Returns predicted gesture label
  
- `model.py` - Alternative model implementation
  - Similar to main.py with different model path
  - Includes model input shape validation
  - Landmark normalization
  
- `model_input.py` - Dual-model implementation
  - Supports both static and dynamic gesture recognition
  - `/predict` endpoint for static images
  - `/predict-video` endpoint for video sequences
  - Handles frame extraction from videos
  - Batch processing for performance
  
- `media.py` - Production-ready implementation
  - Comprehensive error handling
  - Temporary file management
  - Network IP detection (`/network-info` endpoint)
  - Static gesture recognition (`/predict`)
  - Dynamic gesture recognition (`/predict-video`)
  - Confidence scores in responses
  - Logging and debugging

- `test.py` - Test suite for the server

**Generated/Output Files:**
- `annotated_image.jpg` - Image with hand landmarks drawn
- `received_image.jpg` - Debug copy of received image
- `output_image.jpg` - Processed output image

**Environment:**
- `.venv/` - Python virtual environment (excluded from git)

## Technology Stack

### Frontend (Mobile)
- **Framework:** Flutter
- **Language:** Dart
- **Platform:** Android
- **Key Libraries:**
  - Camera plugin for live video capture
  - HTTP client for API communication
  - Flutter TTS for audio output
  - Provider for state management

### Backend (Server)
- **Framework:** Flask
- **Language:** Python
- **ML Libraries:**
  - TensorFlow/Keras - Deep learning models
  - MediaPipe - Hand detection and landmark extraction
  - OpenCV (cv2) - Image processing
  - NumPy - Numerical operations
  - PIL - Image loading
- **Additional:**
  - Flask-CORS - Cross-origin resource sharing
  - Logging - Server logging

## Core Functionality

### Sign Language Recognition System

#### Static Gesture Recognition (Single Frame)
1. Mobile app captures image from camera
2. Image sent to `/predict` endpoint
3. Server extracts hand landmarks using MediaPipe
4. Landmarks passed to MobileViT model
5. Model predicts gesture label (A-Z, 1-9)
6. Confidence score returned
7. Mobile app displays result and speaks it aloud

#### Dynamic Gesture Recognition (Video Sequence)
1. Mobile app records video of sign language
2. Video sent to `/predict-video` endpoint
3. Server extracts 30 frames from video
4. Hand landmarks extracted from each frame
5. Frame sequence passed to dynamic model
6. Model predicts dynamic gesture (Doctor, Help, Hot, Lose, Pain, Thief)
7. Confidence score returned
8. Mobile app displays result

### Gesture Labels

**Static Gestures (Single Frame):**
- Numbers: 1, 2, 3, 4, 5, 6, 7, 8, 9
- Letters: A-Z (32 total classes)

**Dynamic Gestures (Video Sequence):**
- Doctor
- Help
- Hot
- Lose
- Pain
- Thief

### Hand Landmark Extraction
- MediaPipe detects up to 2 hands per image
- Each hand has 21 landmarks (x, y, z coordinates)
- Total: 42 landmarks (21 per hand) or padded with zeros if only 1 hand
- Landmarks normalized to [0, 1] range

## API Endpoints

### Flask Server (Port 5000)

| Endpoint | Method | Purpose | Input | Output |
|----------|--------|---------|-------|--------|
| `/` | GET | Health check | None | "Server is up and running....." |
| `/predict` | POST | Static gesture recognition | Image file (PNG/JPG) | `{"gesture": "A", "confidence": 0.95}` |
| `/predict-video` | POST | Dynamic gesture recognition | Video file (MP4/MOV/AVI) | `{"gesture": "Help", "confidence": 0.87}` |
| `/network-info` | GET | Network configuration | None | `{"ip": "192.168.x.x", "status": "ready", "connect_url": "..."}` |

## Build and Deployment

### Flutter App
- Built with Flutter SDK
- Targets Android platform
- Uses Gradle build system
- Supports multiple architectures

### Flask Server
- Python-based server
- Runs on `0.0.0.0:5000` (all interfaces)
- Requires TensorFlow, MediaPipe, OpenCV
- Models loaded from local paths (currently hardcoded)

## Development Setup

### Prerequisites
- Flutter SDK (3.7.0+)
- Android SDK/NDK
- Python 3.x
- Git

### Installation Steps

1. **Flutter App:**
   ```bash
   cd android_app/test_123
   flutter pub get
   flutter run
   ```

2. **Flask Server:**
   ```bash
   cd Server/flask_server
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install flask flask-cors tensorflow mediapipe opencv-python pillow numpy
   python media.py  # or main.py, model.py, model_input.py
   ```

## Model Information

### Static Model
- **Name:** MobileViT Landmarks Model
- **Input:** Hand landmarks (1, 42, 3) - 42 landmarks with x,y,z coordinates
- **Output:** 32 classes (A-Z, 1-9)
- **Path:** `C:\Users\gouth\Downloads\mobilevit_landmarks_model (4).h5`

### Dynamic Model
- **Name:** Dynamic Sign Language Model
- **Input:** Video frames (1, 30, 84) - 30 frames with 42 landmarks × 2 coordinates (x,y)
- **Output:** 6 classes (Doctor, Help, Hot, Lose, Pain, Thief)
- **Path:** `C:\Users\gouth\Downloads\dynamic_sign_language_model.h5`

## Current Implementation Status

### Completed
- ✅ Hand detection using MediaPipe
- ✅ Landmark extraction (21 points per hand)
- ✅ Static gesture recognition (single frame)
- ✅ Dynamic gesture recognition (video sequence)
- ✅ Image annotation with landmarks
- ✅ Error handling and logging
- ✅ CORS support for mobile app
- ✅ Confidence score calculation
- ✅ Network IP detection
- ✅ Temporary file management

### In Progress / TODO
- [ ] Create `requirements.txt` for Python dependencies
- [ ] Move model paths to environment variables
- [ ] Add comprehensive unit tests
- [ ] Implement caching for repeated gestures
- [ ] Add gesture history/logging
- [ ] Optimize model loading (load once at startup)
- [ ] Add batch processing for multiple images
- [ ] Implement gesture confidence thresholds
- [ ] Add support for custom gesture training
- [ ] Create comprehensive API documentation
- [ ] Set up CI/CD pipeline
- [ ] Performance optimization and benchmarking

## Known Issues / Limitations

1. **Model Paths:** Currently hardcoded to Windows user directory
2. **Single Model Instance:** Models loaded per request (should be loaded once)
3. **Video Duration:** Limited to 10 seconds max
4. **Frame Count:** Fixed to 30 frames for dynamic recognition
5. **Gesture Set:** Limited to predefined labels (no custom gestures)
6. **Confidence Threshold:** No minimum confidence filtering

## File Organization

```
project/
├── android_app/test_123/          # Flutter mobile app
│   ├── lib/
│   │   ├── main.dart
│   │   ├── screens/
│   │   └── widgets/
│   ├── android/                   # Android-specific code
│   ├── assets/
│   ├── pubspec.yaml
│   └── test/
├── Server/flask_server/           # Python backend
│   ├── main.py
│   ├── model.py
│   ├── model_input.py
│   ├── media.py
│   ├── test.py
│   └── readme.txt
├── .gitignore
└── PROJECT_DOCUMENTATION.md
```

## Next Steps

1. **Environment Setup:**
   - Create `requirements.txt` with all Python dependencies
   - Move model paths to environment variables
   - Document model download/setup process

2. **Code Quality:**
   - Add comprehensive unit tests
   - Add integration tests
   - Set up linting and code formatting

3. **Performance:**
   - Load models once at server startup
   - Implement caching for repeated gestures
   - Optimize landmark extraction

4. **Features:**
   - Add gesture history tracking
   - Implement confidence thresholds
   - Add support for custom gesture training
   - Create gesture database

5. **Documentation:**
   - API documentation (Swagger/OpenAPI)
   - Model training documentation
   - Deployment guide
   - User manual

## Notes

- The project is a sign language recognition system using deep learning
- Supports both static (single frame) and dynamic (video) gesture recognition
- Uses MediaPipe for robust hand detection
- Mobile-first approach with backend API
- Currently in development with hardcoded paths and model loading per request
