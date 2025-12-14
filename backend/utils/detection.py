import cv2
import numpy as np
from mtcnn import MTCNN


detector = MTCNN()

def detect_face(image):

    try:
        
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        
        detections = detector.detect_faces(rgb_image)
        
        if len(detections) == 0:
            return None
        
        
        if len(detections) > 1:
            detections = sorted(detections, key=lambda x: x['confidence'], reverse=True)
        
        
        x, y, w, h = detections[0]['box']
        
        
        x, y = abs(x), abs(y)
        
        return (x, y, w, h)
        
    except Exception as e:
        print(f"Error in MTCNN face detection: {e}")
       
        return detect_face_haar(image)

def detect_face_haar(image):
    
    try:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        )
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )
        
        if len(faces) == 0:
            return None
        
        if len(faces) > 1:
            faces = sorted(faces, key=lambda x: x[2] * x[3], reverse=True)
        
        return faces[0]
        
    except Exception as e:
        print(f"Error in Haar Cascade detection: {e}")
        return None


