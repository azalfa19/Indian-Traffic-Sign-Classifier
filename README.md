# 🚦 Indian Traffic Sign Classifier

## 📌 Problem Statement

Road safety is a critical concern in India due to the large number of vehicles and diverse traffic conditions. Traffic signs play an important role in guiding drivers and preventing accidents. However, manual recognition of traffic signs can sometimes be slow or inaccurate, especially in complex environments.

The objective of this project is to develop an **Indian Traffic Sign Classifier** using Machine Learning that can automatically identify and classify traffic signs from images. This system can assist drivers and can be further extended to autonomous vehicles and driver assistance systems.

---

## 🎯 Objectives

* To build a model that can classify different types of Indian traffic signs.
* To use real-world dataset for training the model.
* To implement an easy-to-use GUI where users can upload images and get predictions.
* To improve understanding of Machine Learning concepts like classification and image processing.

---

## 🧠 Approach

1. **Dataset Collection**

   * Used Indian Traffic Sign Dataset from Kaggle.
   * Dataset contains multiple classes of traffic signs.

2. **Data Preprocessing**

   * Images resized to fixed dimensions (32x32).
   * Converted to grayscale.
   * Normalized pixel values.

3. **Model Training**

   * Used Machine Learning algorithm (K-Nearest Neighbors / Random Forest).
   * Trained model on processed image data.

4. **Model Saving**

   * Saved trained model using `pickle`.

5. **GUI Development**

   * Built using Tkinter.
   * Allows users to upload an image and view prediction.

---

## 🛠️ Technologies Used

* Python
* OpenCV
* NumPy
* Scikit-learn
* Tkinter

---

## 📊 Features

* Image upload functionality
* Real-time prediction
* User-friendly GUI
* Uses real dataset
* Lightweight and easy to run

---

## ⚠️ Limitations

* Uses basic ML algorithms instead of deep learning (CNN).
* Accuracy may vary for unseen or complex images.
* Limited to dataset classes.

---

## 🚀 Future Scope

* Implement Convolutional Neural Networks (CNN) for higher accuracy.
* Add real-time detection using webcam.
* Improve UI with better design and visualization.
* Deploy as a web or mobile application.

---

## ✅ Conclusion

This project demonstrates how Machine Learning can be used to solve real-world problems like traffic sign recognition. It provides a foundation for building more advanced intelligent systems in the field of computer vision and autonomous driving.
