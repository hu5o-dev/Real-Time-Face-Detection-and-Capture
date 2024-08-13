# 🎥 Real-Time Face Detection and Capture

Welcome to the **Real-Time Face Detection and Capture** project! 🚀 This project utilizes state-of-the-art face detection technology to capture and save face images in real-time using your webcam. Perfect for applications in security, attendance systems, or just for fun! 😄

## 📸 Features

- **Real-Time Face Detection:** Uses the `insightface` library to detect faces in real-time.
- **Automatic Image Saving:** Captures and saves detected faces with timestamps.
- **System Monitoring:** Keeps track of CPU and memory usage during operation.
- **Custom Tkinter UI:** A sleek graphical interface to start the face capture process.

## 🛠️ Installation

Make sure you have the required dependencies installed. You can set up the project using `pip`:

```bash
pip install opencv-python-headless numpy psutil insightface customtkinter
```

## 🚀 Getting Started

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/hu5o-dev/Real-Time-Face-Detection-and-Capture.git
   cd Real-Time-Face-Detection-and-Capture
   ```

2. **Run the Application:**

   Execute the following command to start the application:

   ```bash
   python main.py
   ```

   This will open a graphical user interface. Click "Start Capture" to begin capturing faces! 📷
   ![image](https://github.com/user-attachments/assets/94678614-08e2-4855-aafc-2ca66ccbfdf3)


## 📜 Code Overview

Here's a brief rundown of what the code does:

1. **Directory Setup:**
   Ensures a directory exists to save captured face images.

2. **Face Detection Initialization:**
   Sets up the `insightface` model for detecting faces.

3. **System Monitoring:**
   Monitors CPU and memory usage using `psutil`.

4. **Face Capture:**
   Opens the webcam, detects faces, and saves images with timestamps.

5. **Custom UI:**
   Provides a user interface to start the face capture process.

## ⚙️ Code Breakdown

- **`monitor_system()`:** Monitors CPU and memory usage.
- **`save_face_image(face_img)`:** Saves the detected face image to the filesystem.
- **`capture_faces()`:** Handles real-time face detection and image saving.
- **`create_ui()`:** Sets up the custom Tkinter UI for user interaction.

## 🎨 Customization

Feel free to customize the face detection model or adjust the UI as per your needs. For example, you can switch to a different face detection model or modify the UI layout.

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 📢 Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements or fixes.

## 🌟 Support

If you have any questions or run into issues, feel free to open an issue on GitHub or contact me directly.

---

Happy coding! 🚀😃

[![GitHub stars](https://img.shields.io/github/stars/hu5o-dev/Real-Time-Face-Detection-and-Capture?style=social)](https://github.com/hu5o/dev/Real-Time-Face-Detection-and-Capture)

