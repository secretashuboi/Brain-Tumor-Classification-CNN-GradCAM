\# 🧠 Brain Tumor Classification Using CNN \& ResNet18 with Grad-CAM



\[!\[Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)](https://www.python.org/)

\[!\[PyTorch](https://img.shields.io/badge/PyTorch-Deep%20Learning-ee4c2c?logo=pytorch)](https://pytorch.org/)

\[!\[Streamlit](https://img.shields.io/badge/Streamlit-Live%20Demo-ff4b4b?logo=streamlit)](https://streamlit.io/)



A deep learning project for classifying brain MRI images into four categories using CNN-based models, with \*\*ResNet18\*\* as the final model and \*\*Grad-CAM\*\* for explainable AI visualization.



\---



\## 🚀 Live Demo



👉 \*\*\[Open the Live Streamlit Application](https://brain-tumor-classification-cnn-gradcam-by-ashu.streamlit.app/)\*\*



Upload a brain MRI image to obtain a predicted class, confidence score, class probabilities, and Grad-CAM visualization.



> ⚠️ \*\*Medical Disclaimer:\*\* This project is intended for research and educational purposes only. It is not a medical diagnostic system and should not be used for clinical decision-making.



\---



\## 📌 Project Overview



This project explores \*\*brain tumor classification from MRI images\*\* using convolutional neural networks and transfer learning.



Multiple models were experimented with before selecting \*\*ResNet18\*\* as the final model.



The system classifies MRI images into four categories:



\- 🧠 Glioma

\- 🧠 Meningioma

\- ✅ No Tumor

\- 🧠 Pituitary



The final application also uses \*\*Grad-CAM (Gradient-weighted Class Activation Mapping)\*\* to visualize image regions that contributed to the model's prediction.



\---



\## 📊 Model Performance



| Model | Test Accuracy |

|---|---:|

| CNN Experiment 1 | 75.00% |

| CNN Experiment 2 | 76.69% |

| \*\*ResNet18 (Final Model)\*\* | \*\*94.44%\*\* |



\### ResNet18 Results



\- \*\*Validation Accuracy:\*\* 98.66%

\- \*\*Test Accuracy:\*\* 94.44%

\- \*\*Test Loss:\*\* 0.3431

\- \*\*Correct Test Predictions:\*\* 1511 / 1600



ResNet18 significantly outperformed the two custom CNN experiments and was selected as the final model for deployment.



\---



\## 🖼️ Application Screenshots



\### 1. Main Interface



!\[Main Interface](assets/main-interface.png)



The Streamlit application provides an interactive interface for uploading brain MRI images and running the trained ResNet18 model.



\### 2. Prediction Results \& Class Probabilities



!\[Prediction Results](assets/prediction-results.png)



The application displays the predicted tumor class, confidence score, and probability distribution across all four classes.



\### 3. Grad-CAM Explainability



!\[Grad-CAM Explainability](assets/gradcam-explainability.png)



Grad-CAM highlights the regions of the MRI image that contributed most strongly to the model's prediction.



\---



\## 🧠 Model Architecture



The final model uses \*\*ResNet18\*\* with a modified fully connected layer for four-class classification.



\- \*\*Architecture:\*\* ResNet18

\- \*\*Input:\*\* 224 × 224 RGB image

\- \*\*Output Classes:\*\* 4

\- \*\*Final Layer:\*\* Fully connected layer with 4 outputs

\- \*\*Framework:\*\* PyTorch

\- \*\*Explainability:\*\* Grad-CAM



\### Image Preprocessing



Input MRI images are:



1\. Converted to RGB

2\. Resized to \*\*224 × 224\*\*

3\. Converted to tensors

4\. Normalized using ImageNet mean and standard deviation



\---



\## 🔥 Grad-CAM Explainability



\*\*Grad-CAM\*\* provides a visual explanation of the model's prediction by generating a class-specific activation map from the final convolutional layers.



The application provides:



\- 🔥 Grad-CAM heatmap

\- 🧠 Heatmap overlay on the original MRI

\- 🎯 Predicted class

\- 📊 Prediction confidence

\- 📈 Class probability distribution



This makes the model's prediction more interpretable by showing which regions contributed to the classification.



\---



\## 📂 Dataset



The project uses the \*\*Brain Tumor MRI Dataset\*\* from Kaggle.



\*\*Dataset:\*\* Masoud Nickparvar — Brain Tumor MRI Dataset



\### Classes



\- Glioma

\- Meningioma

\- No Tumor

\- Pituitary



\### Dataset Size



\- \*\*Training Images:\*\* 5,600

\- \*\*Testing Images:\*\* 1,600

\- \*\*Total Images:\*\* 7,200



Dataset source:



\*\*\[Brain Tumor MRI Dataset — Kaggle](https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset)\*\*



\---



\## 🛠️ Technologies Used



\- Python

\- PyTorch

\- Torchvision

\- NumPy

\- OpenCV

\- Pillow

\- Matplotlib

\- Streamlit

\- Jupyter Notebook

\- Google Colab



\---



\## 📁 Project Structure



```text

Brain-Tumor-Classification-CNN-GradCAM/

│

├── app.py

├── requirements.txt

├── README.md

├── .gitignore

│

├── models/

│   └── best\_brain\_tumor\_resnet18.pth

│

├── notebooks/

│   └── Brain\_Tumor\_Classification\_Using\_CNN\_and\_GradCAM.ipynb

│

├── src/

│   └── gradcam.py

│

└── assets/

&#x20;   ├── main-interface.png

&#x20;   ├── prediction-results.png

&#x20;   └── gradcam-explainability.png

