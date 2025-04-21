# Face Mask Detection using YOLOv5

This project uses a custom-trained YOLOv5 model to detect whether a person is wearing a face mask or not in real-time using a webcam.

## 📸 Demo
The application opens your webcam and performs live detection. It labels people with:
- ✅ **"with mask"** (Green box)
- ❌ **"no mask"** (Red box)

## 🧠 Model
- Model: YOLOv5 (custom)
- Framework: PyTorch
- Pre-trained weights: `detect-person.pt`

## 🚀 How to Run
python cam.py

## 🧪 Sample Output 


### With Mask
![With Mask](Images/With%20Mask.jpg)


### Without Mask
![No Mask](Images/No%20Mask.jpg)


