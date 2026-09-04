\# 🧠 Brain Tumor Classification Using CNN \& ResNet18 with Grad-CAM



A deep learning-based brain MRI classification system that classifies MRI images into four categories using Convolutional Neural Networks and ResNet18. The project also integrates Grad-CAM (Gradient-weighted Class Activation Mapping) to provide visual explanations for model predictions.



\## 🚀 Project Overview



This project explores multiple deep learning experiments for classifying brain MRI images into:



\- Glioma

\- Meningioma

\- No Tumor

\- Pituitary



Three experiments were conducted, progressively improving the classification performance.



The final ResNet18 model achieved:



\*\*94.44% Test Accuracy\*\*



The trained model is integrated with a Streamlit application that allows users to upload an MRI image and receive a prediction, confidence score, class probabilities, and Grad-CAM visualization.



\---



\## 📊 Model Performance



| Model | Test Accuracy |

|---|---:|

| CNN Experiment 1 | 75.00% |

| CNN Experiment 2 | 76.69% |

| ResNet18 | \*\*94.44%\*\* |



\### ResNet18 Results



\- Test Loss: \*\*0.3431\*\*

\- Test Accuracy: \*\*94.44%\*\*

\- Correct Predictions: \*\*1511 / 1600\*\*

\- Best Validation Accuracy: \*\*98.66%\*\*



\---



\## 🧠 Model Architecture



The final model uses \*\*ResNet18\*\* with a modified final fully connected layer for four-class classification.



\### Input



\- RGB MRI image

\- Resized to \*\*224 × 224\*\*

\- ImageNet normalization



\### Output Classes



```text

0 → glioma

1 → meningioma

2 → notumor

3 → pituitary

