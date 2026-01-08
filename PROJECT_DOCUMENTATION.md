# Project Documentation

## Overview
This is a mini-project consisting of a Flutter mobile application (Android) and a Python Flask backend server. The application appears to be designed for image processing with camera integration.

## Project Structure

### Root Directories

#### `/android_app/test_123/` - Flutter Mobile Application
A Flutter-based Android application with the following structure:

**Key Directories:**
- `lib/` - Dart source code
  - `main.dart` - Application entry point
  - `screens/` - Screen components
    - `home_screen.dart` - Main home screen
  - `widgets/` - Reusable UI components
    - `camera_preview.dart` - Camera preview widget
    - `control_buttons.dart` - Control button widgets
    - `homepage.dart` - Homepage widget
    - `output_box.dart` - Output display widget
    - `progress_bar.dart` - Progress indicator widget
    - `settings_sheet.dart` - Settings UI component
  - `CONTEXT.txt` - Context/documentation file

- `android/` - Android-specific configuration and build files
  - `app/` - Main app module
    - `src/main/` - Android source code
    - `.cxx/` - CMake build artifacts
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
- `.metadata` - Flutter project metadata
- `.flutter-plugins` - Flutter plugin references
- `.flutter-plugins-dependencies` - Plugin dependency tracking

#### `/Server/flask_server/` - Python Backend Server
A Flask-based Python server for backend processing:

**Key Files:**
- `main.py` - Flask application entry point and API endpoints
- `model.py` - Machine learning model implementation
- `model_input.py` - Model input handling and preprocessing
- `media.py` - Media/image processing utilities
- `test.py` - Test suite for the server

**Generated/Output Files:**
- `annotated_image.jpg` - Output image with annotations
- `output_image.jpg` - Processed output image

**Documentation:**
- `readme.txt` - Server documentation

**Environment:**
- `.venv/` - Python virtual environment (excluded from git)
- `.idea/` - IDE configuration (excluded from git)

## Technology Stack

### Frontend (Mobile)
- **Framework:** Flutter
- **Language:** Dart
- **Platform:** Android (primary)
- **Key Features:**
  - Camera integration
  - Real-time preview
  - Settings management
  - Progress tracking

### Backend (Server)
- **Framework:** Flask
- **Language:** Python
- **Key Features:**
  - Image processing
  - Model inference
  - Media handling
  - API endpoints

## Functionality Overview

### Mobile App Features
1. **Camera Preview** - Live camera feed display
2. **Image Capture** - Capture images from camera
3. **Settings** - Configurable application settings
4. **Progress Tracking** - Visual progress indicators
5. **Output Display** - Show processed results

### Backend Server Features
1. **Image Processing** - Process and annotate images
2. **Model Inference** - Run ML model on input data
3. **Media Handling** - Handle image uploads and processing
4. **API Endpoints** - RESTful API for mobile app communication

## Build and Deployment

### Flutter App
- Built with Flutter SDK
- Targets Android platform
- Uses Gradle build system
- Supports multiple architectures (arm64-v8a, armeabi-v7a, x86, x86_64)

### Flask Server
- Python-based server
- Requires virtual environment setup
- Dependencies managed via pip

## Development Setup

### Prerequisites
- Flutter SDK
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
   pip install -r requirements.txt  # If requirements.txt exists
   python main.py
   ```

## Git Configuration

- Repository initialized with git
- `.gitignore` configured to exclude:
  - Build artifacts
  - Virtual environments
  - IDE configuration
  - Generated images
  - Cache files
  - OS-specific files

## Next Steps

1. Create `requirements.txt` for Python dependencies
2. Document API endpoints in Flask server
3. Add comprehensive README files
4. Set up CI/CD pipeline
5. Create feature specifications using Kiro specs
6. Implement unit and integration tests

## Notes

- The project appears to be in active development
- Image processing and ML model integration is a core feature
- Mobile-first approach with backend support
- Cross-platform considerations for Android deployment
