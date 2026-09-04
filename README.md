\# 🧠 Brain Tumor Classification Using CNN \& ResNet18 with Grad-CAM



\### 🔬 Deep Learning Based Brain MRI Classification \& Explainable AI System



\*\*CNN • ResNet18 • Transfer Learning • Grad-CAM • PyTorch • Computer Vision • Streamlit\*\*



\[!\[Python](https://img.shields.io/badge/Python-3.x-blue?logo=python\&logoColor=white)](https://www.python.org/)

\[!\[PyTorch](https://img.shields.io/badge/PyTorch-Deep%20Learning-ee4c2c?logo=pytorch\&logoColor=white)](https://pytorch.org/)

\[!\[Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit\&logoColor=white)](https://streamlit.io/)

\[!\[ResNet18](https://img.shields.io/badge/Model-ResNet18-orange)](https://pytorch.org/vision/stable/models/generated/torchvision.models.resnet18.html)

\[!\[Grad-CAM](https://img.shields.io/badge/Explainability-Grad--CAM-purple)](https://arxiv.org/abs/1610.02391)

\[!\[Accuracy](https://img.shields.io/badge/Test%20Accuracy-94.44%25-brightgreen)](https://github.com/secretashuboi/Brain-Tumor-Classification-CNN-GradCAM)



\---



\## 🌟 Overview



\*\*Brain Tumor Classification\*\* is a deep learning based brain MRI classification system designed to classify MRI images into four categories:



\- \*\*Glioma\*\*

\- \*\*Meningioma\*\*

\- \*\*No Tumor\*\*

\- \*\*Pituitary\*\*



The project explores multiple CNN based experiments and compares their performance with a \*\*ResNet18 transfer learning model\*\*.



The final ResNet18 model achieved a \*\*94.44% test accuracy\*\* on 1600 test images.



To make the model more interpretable, the project integrates \*\*Grad-CAM (Gradient-weighted Class Activation Mapping)\*\* to visualize the regions of an MRI image that contributed to the model's prediction.



The trained model is deployed through an interactive \*\*Streamlit web application\*\*.



\---



\## 🚀 Live Demo



\### 🖥️ Try the Application



\*\*\[Open Brain Tumor Classification App](https://brain-tumor-classification-cnn-gradcam-by-ashu.streamlit.app/)\*\*



The application allows users to:



\- Upload a brain MRI image

\- Predict the tumor category

\- View prediction confidence

\- View class probability distribution

\- Generate Grad-CAM heatmaps

\- View Grad-CAM overlays



> ⚠️ \*\*Medical Disclaimer:\*\* This application is intended for educational and research purposes only. It is not a clinically validated diagnostic system and should not be used for medical diagnosis or treatment decisions.



\---



\## 📊 Model Performance



Three deep learning experiments were conducted during the development of the project.



| Model | Test Accuracy |

|---|---:|

| CNN Experiment 1 | 75.00% |

| CNN Experiment 2 | 76.69% |

| \*\*ResNet18\*\* | \*\*94.44%\*\* |



\### 🏆 Final ResNet18 Results



| Metric | Result |

|---|---:|

| Best Validation Accuracy | \*\*98.66%\*\* |

| Test Accuracy | \*\*94.44%\*\* |

| Test Loss | \*\*0.3431\*\* |

| Correct Predictions | \*\*1511 / 1600\*\* |



The ResNet18 model significantly outperformed the two custom CNN experiments and was selected as the final model for deployment.



\---



\## 🧠 Classification Categories



The final model performs four-class classification:



| Class | Category |

|---|---|

| 0 | Glioma |

| 1 | Meningioma |

| 2 | No Tumor |

| 3 | Pituitary |



\---



\## 🖥️ Application Screenshots



\### 📌 Main Application Interface



!\[Main Application Interface](assets/main-interface.png)



The Streamlit application provides an interactive interface where users can upload a brain MRI image and run the trained ResNet18 model.



\---



\### 🎯 Prediction Results



!\[Prediction Results](assets/prediction-results.png)



The application displays the predicted class, prediction confidence, and probability distribution across all four categories.



\---



\### 🔥 Grad-CAM Explainability



!\[Grad-CAM Explainability](assets/gradcam-explainability.png)



Grad-CAM highlights important regions of the MRI image that contributed to the model's prediction.



This provides a visual explanation of the model's decision and improves interpretability.



\---



\## 🔬 System Architecture



```text

&#x20;                   Brain MRI Image

&#x20;                          |

&#x20;                          v

&#x20;                 Image Preprocessing

&#x20;                          |

&#x20;                          v

&#x20;                   Resize 224 x 224

&#x20;                          |

&#x20;                          v

&#x20;                 ImageNet Normalization

&#x20;                          |

&#x20;                          v

&#x20;                      ResNet18

&#x20;                          |

&#x20;                          v

&#x20;                 Feature Extraction

&#x20;                          |

&#x20;                          v

&#x20;               Modified FC Layer

&#x20;                          |

&#x20;                          v

&#x20;                 Four Class Prediction

&#x20;                          |

&#x20;             +------------+------------+

&#x20;             |            |            |

&#x20;             v            v            v

&#x20;          Glioma     Meningioma    No Tumor

&#x20;                          |

&#x20;                          v

&#x20;                      Pituitary

&#x20;                          |

&#x20;                          v

&#x20;                 Prediction Confidence

&#x20;                          |

&#x20;                          v

&#x20;                   Grad-CAM Analysis

&#x20;                          |

&#x20;                          v

&#x20;                 Heatmap + Overlay

