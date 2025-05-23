import cv2
import numpy as np
from deepface import DeepFace
import datetime
from tkinter import messagebox, Tk
import pyttsx3

# Initialize speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 160)
engine.setProperty('volume', 0.8)

# Popup to notify user
root = Tk()
root.withdraw()
messagebox.showinfo("Recording", "🔴 Emotion recording started.\n\nPress 'q' to stop.")

# Load model (DeepFace version 0.0.81 uses this form)
print("🔄 Loading DeepFace emotion model...")
model = DeepFace.build_model("Emotion")
emotion_labels = ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral']

# Haar cascade face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Start webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("❌ Webcam access failed.")
    exit()

# Video writer
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
fps = int(cap.get(cv2.CAP_PROP_FPS)) or 24
filename = f"emotion_output_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.avi"
out = cv2.VideoWriter(filename, cv2.VideoWriter_fourcc(*'XVID'), fps, (frame_width, frame_height))

print(f"🎥 Recording to: {filename}\n📌 Press 'q' to stop.")

last_announced = None
announce_delay = 30
frame_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Frame read failed.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces:
        face_roi = gray[y:y+h, x:x+w]
        resized_face = cv2.resize(face_roi, (48, 48))
        normalized = resized_face / 255.0
        reshaped = normalized.reshape(1, 48, 48, 1)

        prediction = model.predict(reshaped)[0]
        emotion_idx = np.argmax(prediction)
        emotion = emotion_labels[emotion_idx]

        # Draw and speak
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)

        if frame_count % announce_delay == 0 and emotion != last_announced:
            engine.say(f"You look {emotion}")
            engine.runAndWait()
            last_announced = emotion

    frame_count += 1
    out.write(frame)
    cv2.imshow('Emotion Detection - Press Q to Quit', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
print("✅ Done. Video saved.")
