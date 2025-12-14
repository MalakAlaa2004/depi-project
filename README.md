
# Face Recognition System

## Overview

This project is a **Face Recognition System** built using **Python**, **Flask**, **MTCNN**, **FaceNet**, and **KNN**. It allows users to **register their face** via a webcam or image upload, and then **recognize faces** in real-time or from images.

The system performs:

* Face detection using **MTCNN**
* Face alignment for better accuracy
* Face embedding extraction using **FaceNet**
* Face recognition using **K-Nearest Neighbors (KNN)**

---

## Features

* **User Registration**: Capture user images and store embeddings.
* **Face Recognition**: Identify registered users from live camera feed or uploaded images.
* **Duplicate Detection**: Detect if a face already exists in the database.
* **Web Interface**: Simple **Flask-based UI** with webcam capture support.
* **Cross-platform**: Works on Windows, Linux, and Mac.

---

## Folder Structure

```
FaceRecognitionApp/
│
├─ backend/                 # Flask backend
│   ├─ app.py               # Main Flask application
│   ├─ utils/
│   │   ├─ detection.py      # Face detection using MTCNN
│   │   ├─ alignment.py     # Face alignment functions
│   │   ├─ embedding.py     # FaceNet embedding generation
│   │   └─ compare.py       # Face recognition and duplicate checking
│   └─ database/            # Stored embeddings
│
├─ frontend/                # Frontend web interface
│   ├─ index.html           # Home page
│   └─ scripts.js           # Frontend scripts for webcam capture
│
├─ requirements.txt         # Python dependencies
└─ README.md                # Project documentation
```

---

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/FaceRecognitionApp.git
cd FaceRecognitionApp
```

2. **Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the Flask server**

```bash
cd backend
python app.py
```

5. **Open the frontend**

* Navigate to `http://localhost:5000` in your browser.

---

## How to Use

### Register a User

1. Go to the **Register** page.
2. Enter your **full name**.
3. Capture your face using the **webcam**.
4. The system will automatically save your face embeddings.

### Recognize a User

1. Go to the **Recognition** page.
2. Use the webcam to capture the face or upload an image.
3. The system will compare the face with stored embeddings and display the **user name** if recognized.

---

## Models Used

| Model       | Purpose                                  |
| ----------- | ---------------------------------------- |
| **MTCNN**   | Face detection and landmark localization |
| **FaceNet** | Generate face embeddings for recognition |
| **KNN**     | Classify faces based on embeddings       |

---

## Requirements

* Python 3.9+
* Flask
* OpenCV
* NumPy
* TensorFlow / PyTorch (for FaceNet)
* scikit-learn

Install all requirements via:

```bash
pip install -r requirements.txt
```

---

## Future Improvements

* Add **multi-face recognition** support in a single frame.
* Implement **real-time alerts** when an unknown face is detected.
* Integrate **database storage** for scaling to hundreds of users.
* Add **login authentication** for the web app.

---

## License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

