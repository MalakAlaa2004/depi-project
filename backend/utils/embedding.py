import cv2
import numpy as np
from keras_facenet import FaceNet


print("Loading FaceNet model...")
facenet_model = FaceNet()
print("FaceNet model loaded successfully!")

def get_embedding(face_image):
    
    try:
        
        if face_image.shape[:2] != (160, 160):
            face_image = cv2.resize(face_image, (160, 160))
        
        
        rgb_face = cv2.cvtColor(face_image, cv2.COLOR_BGR2RGB)
        
        
        face_pixels = np.expand_dims(rgb_face, axis=0)
        
        
        embedding = facenet_model.embeddings(face_pixels)
        
        
        return embedding[0]
        
    except Exception as e:
        print(f"Error in FaceNet embedding extraction: {e}")
        return None

def normalize_embedding(embedding):
    
    try:
        norm = np.linalg.norm(embedding)
        if norm == 0:
            return embedding
        return embedding / norm
    except Exception as e:
        print(f"Error in normalization: {e}")
        return embedding

