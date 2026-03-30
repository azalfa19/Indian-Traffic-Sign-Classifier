import os
import cv2
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier

IMG_SIZE = 32

images = []
labels = []

label_map = {}
current_label = 0

print("Loading dataset...")

data_path = r"C:\Users\AZALFA\.cache\kagglehub\datasets\neelpratiksha\indian-traffic-sign-dataset\versions\1\Indian-Traffic Sign-Dataset\Images"

# Load images
for label in os.listdir(data_path):
    class_folder = os.path.join(data_path, label)
    
    if os.path.isdir(class_folder):
        if label not in label_map:
            label_map[label] = current_label
            current_label += 1
        
        for file in os.listdir(class_folder):
            img_path = os.path.join(class_folder, file)
            
            img = cv2.imread(img_path)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            if img is None:
                continue
            
            img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
            img = img / 255.0   # ✅ normalize
            images.append(img.flatten())
            labels.append(label_map[label])

print("Total images:", len(images))

# Convert to numpy
X = np.array(images)
y = np.array(labels)

# Train model ✅
print("Training model...")
model = RandomForestClassifier(n_estimators=100)
model.fit(X, y)

# Save model ✅ AFTER training
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("labels.pkl", "wb") as f:
    pickle.dump(label_map, f)

print("✅ Model saved successfully!")