# Real-Time Mood Detection using OpenCV & DeepFace

**Final Project – Methods of Research**

**Submitted by: Keneth Campo, Gwyneth Esperat, Chester Sangcap**

**Section: CPE32S34**

This project demonstrates the practical application of computer vision and deep learning in a standalone desktop application. The system performs real-time facial emotion recognition with integrated video recording. It uses OpenCV to capture webcam input, DeepFace for emotion classification, and Tkinter to render an interactive user interface. The application can also process pre-recorded videos for mood detection, supporting both live and offline modes.

---

## Key Features

* **Live Webcam Detection**
  Real-time facial emotion detection and overlay using OpenCV and DeepFace.

* **Offline Video Analysis**
  Users can upload a video file and extract emotion predictions frame-by-frame.

* **Graphical User Interface (GUI)**
  Built with Tkinter, the interface features clear layout and responsive controls.

* **Voice Feedback**
  Detected emotions are announced via a built-in text-to-speech engine.

* **Session Recording**
  All live webcam sessions are saved locally for future analysis.

* **Secure and Offline**
  All processing is done locally, ensuring full data privacy.

---

## Supported Emotions

* Angry
* Disgust
* Fear
* Happy
* Sad
* Surprise
* Neutral

---

## Technologies Used

| Technology   | Purpose                             |
| ------------ | ----------------------------------- |
| Python 3.9+  | Primary programming language        |
| OpenCV       | Video processing and face detection |
| DeepFace     | Emotion recognition model           |
| PIL (Pillow) | Image display in GUI                |
| Tkinter      | GUI framework                       |
| pyttsx3      | Text-to-speech for voice feedback   |

---

## How to Run

1. **Install dependencies**

   ```bash
   pip install opencv-python-headless deepface pyttsx3 pillow numpy
   ```

2. **Use the interface**

   * Click **Start** to begin webcam-based detection.
   * Click **Stop** to end recording.
   * Use **Upload Video** to analyze a local `.mp4` or `.avi` file.

---

## Output

* Video files are saved with a timestamp in the local directory:

  ```
  emotion_output_YYYYMMDD_HHMMSS.avi
  ```

---
