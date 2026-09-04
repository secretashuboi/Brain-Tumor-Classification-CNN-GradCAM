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



\*\*Brain Tumor Classification\*\* is an end-to-end deep learning system designed to classify brain MRI images into four categories:



\- \*\*Glioma\*\*

\- \*\*Meningioma\*\*

\- \*\*No Tumor\*\*

\- \*\*Pituitary\*\*



The project explores custom CNN architectures and compares their performance with a \*\*ResNet18 transfer learning model\*\*.



The final ResNet18 model achieved a \*\*94.44% test accuracy\*\* on 1600 test images.



To improve model interpretability, the system integrates \*\*Grad-CAM (Gradient-weighted Class Activation Mapping)\*\* to visualize the regions of an MRI image that contributed to the model's prediction.



The trained model is deployed through an interactive \*\*Streamlit web application\*\*.



> 💡 \*\*Goal:\*\* Build a practical computer vision system that combines deep learning classification with explainable AI for brain MRI analysis.



\---



\## ✨ Key Features



| Feature | Description |

| ----------------------------------- | ------------------------------------------------ |

| 🧠 \*\*Brain MRI Classification\*\* | Classifies MRI images into four categories |

| 🔬 \*\*ResNet18 Transfer Learning\*\* | Uses a pretrained ResNet18 architecture |

| 📈 \*\*High Classification Accuracy\*\* | Achieves 94.44% test accuracy |

| 🔥 \*\*Grad-CAM Explainability\*\* | Highlights image regions influencing predictions |

| 📊 \*\*Class Probability Analysis\*\* | Displays prediction probabilities for all classes |

| 🖥️ \*\*Interactive Streamlit App\*\* | Provides a simple web-based interface |

| 🖼️ \*\*MRI Image Upload\*\* | Allows users to upload MRI images |

| ⚡ \*\*Real-Time Prediction\*\* | Generates predictions through the deployed model |

| 📚 \*\*Multiple CNN Experiments\*\* | Compares custom CNN models with ResNet18 |

| 💻 \*\*CPU/GPU Compatible\*\* | Supports CUDA when available |



\---



\## 🚀 Live Demo



\### 🖥️ Try the Application



<p align="center">



🔗 \*\*\[Open Brain Tumor Classification App](https://brain-tumor-classification-cnn-gradcam-by-ashu.streamlit.app/)\*\*



</p>



The application allows users to:



\- 🖼️ Upload a brain MRI image

\- 🧠 Predict the tumor category

\- 📊 View prediction confidence

\- 📈 View class probability distribution

\- 🔥 Generate Grad-CAM heatmaps

\- 🖼️ View Grad-CAM overlays

\- 💡 Interpret the model's prediction



> ⚠️ \*\*Medical Disclaimer:\*\* This application is intended for educational and research purposes only. It is not a clinically validated diagnostic system and should not be used for medical diagnosis or treatment decisions.



\---



\# 🏗️ System Architecture



```mermaid

flowchart TD



&#x20;   A\["🖼️ Brain MRI Image"]



&#x20;   B\["🔄 Image Preprocessing"]



&#x20;   C\["📐 Resize 224 × 224"]



&#x20;   D\["🎨 ImageNet Normalization"]



&#x20;   E\["🧠 ResNet18"]



&#x20;   F\["🔬 Feature Extraction"]



&#x20;   G\["🎯 Modified Fully Connected Layer"]



&#x20;   H\["📊 Four-Class Prediction"]



&#x20;   I\["🧠 Glioma"]



&#x20;   J\["🧠 Meningioma"]



&#x20;   K\["✅ No Tumor"]



&#x20;   L\["🧠 Pituitary"]



&#x20;   M\["📈 Prediction Confidence"]



&#x20;   N\["🔥 Grad-CAM"]



&#x20;   O\["🌡️ Heatmap"]



&#x20;   P\["🖼️ Heatmap Overlay"]



&#x20;   A --> B

&#x20;   B --> C

&#x20;   C --> D

&#x20;   D --> E

&#x20;   E --> F

&#x20;   F --> G

&#x20;   G --> H



&#x20;   H --> I

&#x20;   H --> J

&#x20;   H --> K

&#x20;   H --> L



&#x20;   H --> M

&#x20;   H --> N



&#x20;   N --> O

&#x20;   O --> P

