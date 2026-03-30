# 🚦 Indian Traffic Sign Classifier

## 📌 Overview

This project is a Machine Learning-based application that classifies Indian traffic signs from images. It uses a trained model and a simple GUI to allow users to upload an image and get the predicted traffic sign.

---

## 🎯 Features

* 📸 Upload any traffic sign image
* 🤖 Predicts the traffic sign class
* 🖥️ Simple GUI using Tkinter
* ⚡ Fast and lightweight model
* 📊 Uses real-world dataset

---

## 🧠 Technologies Used

* Python
* OpenCV
* NumPy
* Scikit-learn
* Tkinter

---

## 📂 Project Structure

```
AI&Ml/
│
├── train_model.py     # Model training script
├── gui_app.py         # GUI application

```
⚠️ Note: The trained model files (model.pkl, labels.pkl) are not included due to size limits. Please run `train_model.py` to generate them.
---

## 📊 Dataset

* Indian Traffic Sign Dataset (Kaggle)
* Contains 50+ classes of traffic signs
* Images organized in class-wise folders

---

## ⚙️ Installation

### 1. Clone Repository (or download manually)

```
git clone https://github.com/azalfa19/Indian-Traffic-Sign-Classifier
```

### 2. Install Required Libraries

```
pip install opencv-python numpy scikit-learn tkinter
```

---

## 🚀 How to Run

### Step 1: Train Model

```
python train_model.py
```

👉 This will generate:

* `model.pkl`
* `labels.pkl`

---

### Step 2: Run GUI

```
python gui_app.py
```

---

## 🖥️ Usage

1. Click on **Upload Image**
2. Select a traffic sign image
3. View the predicted result

---

## ⚠️ Limitations

* Uses basic ML model (not deep learning)
* Accuracy may vary for new images
* Limited to trained dataset classes

---

## 🚀 Future Improvements

* Implement CNN for higher accuracy
* Add real-time webcam detection
* Improve GUI design
* Deploy as web/mobile app

---

## 👨‍💻 Author

Azalfa S Ansari

---

## 📌 Note

This project is created for educational purposes and demonstrates the use of Machine Learning in image classification.
