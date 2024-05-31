from ultralytics import YOLO
import numpy as np

model_path = '/Users/fadhilahmad/Documents/apl deteksi sayur/model/runs/classify/train/weights/best.pt'
model = YOLO(model_path)

def classify_image(image_path):
    results = model(image_path)
    names_dict = results[0].names
    probs = results[0].probs.data.tolist()
    predicted_class = names_dict[np.argmax(probs)]
    return predicted_class