import tkinter as tk
from tkinter import filedialog
import cv2
import numpy as np
import pickle

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Load label map
with open("labels.pkl", "rb") as f:
    label_map = pickle.load(f)

# Reverse label map
labels = {v: k for k, v in label_map.items()}

IMG_SIZE = 32

# Traffic sign names (basic mapping)
class_names = {
    0: "Speed Limit 20 km/h",
    1: "Speed Limit 30 km/h",
    2: "Speed Limit 50 km/h",
    3: "Speed Limit 60 km/h",
    4: "Speed Limit 70 km/h",
    5: "Speed Limit 80 km/h",
    6: "End of Speed Limit 80",
    7: "Speed Limit 100 km/h",
    8: "Speed Limit 120 km/h",
    9: "No Overtaking",
    10: "No Overtaking Trucks",
    11: "Right of Way",
    12: "Priority Road",
    13: "Yield",
    14: "Stop",
    15: "No Vehicles",
    16: "Heavy Vehicles Prohibited",
    17: "No Entry",
    18: "General Caution",
    19: "Dangerous Curve Left",
    20: "Dangerous Curve Right",
    21: "Double Curve",
    22: "Bumpy Road",
    23: "Slippery Road",
    24: "Road Narrows",
    25: "Road Work",
    26: "Traffic Signals",
    27: "Pedestrian Crossing",
    28: "Children Crossing",
    29: "Bicycle Crossing",
    30: "Snow/Ice Warning",
    31: "Animals Crossing",
    32: "End Restrictions",
    33: "Turn Right Ahead",
    34: "Turn Left Ahead",
    35: "Go Straight",
    36: "Straight or Right",
    37: "Straight or Left",
    38: "Keep Right",
    39: "Keep Left",
    40: "Roundabout",
    41: "End No Overtaking",
    42: "End No Overtaking Trucks"
}

# Prediction function
def predict_image():
    file_path = filedialog.askopenfilename()
    
    if not file_path:
        return
    
    img = cv2.imread(file_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = img / 255.0

    if img is None:
        result_label.config(text="❌ Error loading image")
        return

    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
    img = img.flatten().reshape(1, -1)

    prediction = model.predict(img)[0]
    label = labels[prediction]

    # Convert to actual sign name
    sign_name = class_names.get(int(label), f"Class {label} (Unknown Sign)")

    result_label.config(text=f"🚦 Prediction: {sign_name}")

# GUI setup
root = tk.Tk()
root.title("Indian Traffic Sign Classifier")
root.geometry("420x320")
root.configure(bg="#f0f0f0")

# Title
title = tk.Label(root, text="🚦 Traffic Sign Classifier", 
                 font=("Arial", 18, "bold"), bg="#f0f0f0")
title.pack(pady=20)

# Button
btn = tk.Button(root, text="Upload Image", command=predict_image,
                bg="#007BFF", fg="white", font=("Arial", 12),
                padx=10, pady=5)
btn.pack(pady=20)

# Result label
result_label = tk.Label(root, text="Prediction will appear here",
                        font=("Arial", 12), bg="#f0f0f0")
result_label.pack(pady=20)

# Run GUI
root.mainloop()