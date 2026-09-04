\# 🧠 Brain Tumor Classification Using CNN \& ResNet18 with Grad-CAM



\### 🔬 Deep Learning Based Brain MRI Classification \& Explainable AI System



<p align="center">

&#x20; <b>CNN • ResNet18 • Transfer Learning • Grad-CAM • PyTorch • Computer Vision • Streamlit</b>

</p>



<p align="center">

&#x20; <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python\&logoColor=white" />

&#x20; <img src="https://img.shields.io/badge/PyTorch-Deep%20Learning-ee4c2c?logo=pytorch\&logoColor=white" />

&#x20; <img src="https://img.shields.io/badge/Streamlit-App-red?logo=streamlit\&logoColor=white" />

&#x20; <img src="https://img.shields.io/badge/Model-ResNet18-orange" />

&#x20; <img src="https://img.shields.io/badge/Explainability-Grad--CAM-purple" />

&#x20; <img src="https://img.shields.io/badge/Test%20Accuracy-94.44%25-brightgreen" />

</p>



\---



\## 🌟 Overview



This project presents a \*\*deep learning based brain tumor classification system\*\* designed to classify brain MRI images into four categories:



\- 🧠 Glioma

\- 🧠 Meningioma

\- 🧠 No Tumor

\- 🧠 Pituitary



The project compares a custom CNN with a \*\*ResNet18 transfer learning model\*\* and integrates \*\*Grad-CAM (Gradient-weighted Class Activation Mapping)\*\* to provide visual explanations for model predictions.



The final ResNet18 model achieved a \*\*94.44% test accuracy\*\* on 1,600 unseen MRI images.



\---



\## 🚀 Live Demo



Try the deployed Streamlit application:



👉 \*\*\[Brain Tumor Classification — Live Demo](https://brain-tumor-classification-cnn-gradcam-by-ashu.streamlit.app/)\*\*



The application allows users to:



1\. Upload a brain MRI image

2\. Predict the tumor category

3\. View prediction confidence

4\. View class probabilities

5\. Generate a Grad-CAM heatmap

6\. Understand which regions influenced the prediction



\---



\## 📊 Model Performance



| Model | Best Validation Accuracy | Test Accuracy |

|---|---:|---:|

| Custom CNN | 85.36% | 76.69% |

| ResNet18 | \*\*98.66%\*\* | \*\*94.44%\*\* |



\### 🏆 Final ResNet18 Results



\- \*\*Test Accuracy:\*\* 94.44%

\- \*\*Correct Predictions:\*\* 1,511 / 1,600

\- \*\*Validation Accuracy:\*\* 98.66%

\- \*\*Architecture:\*\* ResNet18

\- \*\*Input Size:\*\* 224 × 224

\- \*\*Framework:\*\* PyTorch

\- \*\*Explainability:\*\* Grad-CAM



\---



\## 🧬 Classification Categories



| Class | Description |

|---|---|

| 🧠 Glioma | Tumor originating from glial cells |

| 🧠 Meningioma | Tumor arising from the meninges |

| 🟢 No Tumor | MRI showing no detected tumor |

| 🧠 Pituitary | Tumor associated with the pituitary gland |



\---



\## 🖥️ Application Screenshots



\### Main Interface



<p align="center">

&#x20; <img src="assets/main-interface.png" width="850"/>

</p>



\### Prediction Results



<p align="center">

&#x20; <img src="assets/prediction-results.png" width="850"/>

</p>



\### Grad-CAM Explainability



<p align="center">

&#x20; <img src="assets/gradcam-explainability.png" width="850"/>

</p>



\---



\## 🏗️ System Architecture



```mermaid

flowchart TD



&#x20;   A\[Brain MRI Dataset] --> B\[Data Preprocessing]



&#x20;   B --> C\[Resize Images to 224x224]



&#x20;   C --> D\[Train Validation Split]



&#x20;   D --> E\[Custom CNN]

&#x20;   D --> F\[ResNet18 Transfer Learning]



&#x20;   E --> G\[Model Evaluation]

&#x20;   F --> G



&#x20;   G --> H\[Best Model: ResNet18]



&#x20;   H --> I\[Brain Tumor Prediction]



&#x20;   I --> J\[Class Probabilities]



&#x20;   I --> K\[Grad-CAM]



&#x20;   K --> L\[Heatmap Visualization]



&#x20;   J --> M\[Streamlit Application]

&#x20;   L --> M

