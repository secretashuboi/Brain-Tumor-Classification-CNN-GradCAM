\# 🧠 Brain Tumor Classification Using CNN \& ResNet18 with Grad-CAM



A deep learning-based brain MRI classification system that classifies MRI images into four categories using Convolutional Neural Networks and ResNet18. The project also integrates \*\*Grad-CAM (Gradient-weighted Class Activation Mapping)\*\* to provide visual explanations for model predictions.



\---



\## 🚀 Live Demo



👉 \*\*\[Try the Live Streamlit Application](https://brain-tumor-classification-cnn-gradcam-by-ashu.streamlit.app/)\*\*



The deployed application allows users to upload a brain MRI image and receive:



\- Predicted tumor class

\- Prediction confidence

\- Class probability distribution

\- Grad-CAM heatmap

\- Grad-CAM overlay visualization



> ⚠️ \*\*Medical Disclaimer:\*\* This application is intended for research and educational purposes only. It is not a medical diagnostic system and should not be used for clinical decision-making.



\---



\## 📌 Project Overview



This project explores multiple deep learning experiments for classifying brain MRI images into four categories:



\- \*\*Glioma\*\*

\- \*\*Meningioma\*\*

\- \*\*No Tumor\*\*

\- \*\*Pituitary\*\*



Three experiments were conducted, progressively improving the classification performance.



The final \*\*ResNet18\*\* model achieved:



\### 🎯 94.44% Test Accuracy



The trained model is integrated with a \*\*Streamlit\*\* web application for interactive MRI classification and explainable AI visualization using Grad-CAM.



\---



\## 📊 Model Performance



| Model | Test Accuracy |

|---|---:|

| CNN Experiment 1 | 75.00% |

| CNN Experiment 2 | 76.69% |

| \*\*ResNet18\*\* | \*\*94.44%\*\* |



\### ResNet18 Results



\- \*\*Test Loss:\*\* 0.3431

\- \*\*Test Accuracy:\*\* 94.44%

\- \*\*Correct Predictions:\*\* 1511 / 1600

\- \*\*Best Validation Accuracy:\*\* 98.66%



The ResNet18 model significantly outperformed the two custom CNN experiments and was selected as the final model for deployment.



\---



\## 🖼️ Application Screenshots



\### 1. Main Application Interface



!\[Main Application Interface](assets/main-interface.png)



The Streamlit application provides an interactive interface where users can upload a brain MRI image for classification.



\---



\### 2. Prediction Results \& Class Probabilities



!\[Prediction Results](assets/prediction-results.png)



The application displays the predicted class, confidence score, and probability distribution across all four tumor categories.



\---



\### 3. Grad-CAM Explainability



!\[Grad-CAM Explainability](assets/gradcam-explainability.png)



Grad-CAM provides a visual explanation of the prediction by highlighting image regions that contributed to the model's classification.



\---



\## 🧠 Model Architecture



The final model uses \*\*ResNet18\*\* with a modified final fully connected layer for four-class classification.



\### Input



\- \*\*Image Size:\*\* 224 × 224

\- \*\*Channels:\*\* 3 (RGB)

\- \*\*Normalization:\*\* ImageNet mean and standard deviation



\### Architecture



```text

Brain MRI Image

&#x20;      │

&#x20;      ▼

Image Preprocessing

&#x20;      │

&#x20;      ▼

ResNet18

&#x20;      │

&#x20;      ▼

Modified Fully Connected Layer

&#x20;      │

&#x20;      ▼

4-Class Prediction

&#x20;      │

&#x20;      ├── Glioma

&#x20;      ├── Meningioma

&#x20;      ├── No Tumor

&#x20;      └── Pituitary

&#x20;      │

&#x20;      ▼

Grad-CAM Explainability

