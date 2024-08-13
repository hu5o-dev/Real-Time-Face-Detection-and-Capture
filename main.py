import cv2
import os
import psutil
import numpy as np
from insightface.app import FaceAnalysis
from customtkinter import CTk, CTkLabel, CTkButton
from tkinter import messagebox
from datetime import datetime


base_dir = "captured_faces"
os.makedirs(base_dir, exist_ok=True)


face_app = FaceAnalysis(name='buffalo_l', providers=['CPUExecutionProvider'])
face_app.prepare(ctx_id=0, det_size=(640, 640))


person_id = 1


def monitor_system():
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    print(f"CPU Usage: {cpu_usage}% | Memory Usage: {memory_usage}%")


def save_face_image(face_img):
    global person_id
    person_dir = os.path.join(base_dir, f"person_{person_id}")
    os.makedirs(person_dir, exist_ok=True)
    img_name = os.path.join(person_dir, f"face_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png")
    cv2.imwrite(img_name, face_img)
    print(f"Saved image: {img_name}")


def capture_faces():
    global person_id

    
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        messagebox.showerror("Error", "No camera detected!")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture image.")
            break

        
        faces = face_app.get(frame)
        if not faces:
            print("No faces detected.")
        
        for face in faces:
            
            bbox = face.bbox.astype(int)
            cv2.rectangle(frame, (bbox[0], bbox[1]), (bbox[2], bbox[3]), (0, 255, 0), 2)

            
            x1, y1, x2, y2 = bbox
            face_img = frame[y1:y2, x1:x2]

           
            if face_img is not None and face_img.size > 0:
                try:
                    
                    print(f"Face image shape: {face_img.shape}, dtype: {face_img.dtype}")
                    if face_img.shape[0] > 0 and face_img.shape[1] > 0:
                        save_face_image(face_img)
                    else:
                        print("Warning: Face image has invalid dimensions.")
                except Exception as e:
                    print(f"Error saving image: {e}")
            else:
                print("Warning: Empty or invalid face image, skipping save.")

        
        cv2.imshow("Real-Time Face Detection", frame)

        
        monitor_system()

        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


def create_ui():
    app = CTk()
    app.geometry("300x150")
    app.title("Face Capture")

    label = CTkLabel(app, text="Click to Start Face Capture")
    label.pack(pady=20)

    def start_capture():
        try:
            capture_faces()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    start_button = CTkButton(app, text="Start Capture", command=start_capture)
    start_button.pack(pady=20)

    app.mainloop()

if __name__ == "__main__":
    create_ui()
