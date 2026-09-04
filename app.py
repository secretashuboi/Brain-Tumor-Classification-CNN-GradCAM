import streamlit as st
import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image
import numpy as np
import cv2
import os
import sys


# ============================================================
# Import Grad-CAM
# ============================================================

sys.path.append("src")

from gradcam import GradCAM


# ============================================================
# Page Configuration
# ============================================================

st.set_page_config(
    page_title="Brain Tumor MRI AI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# Custom Styling
# ============================================================

st.markdown(
    """
    <style>

    .main-title {
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 19px;
        color: #666666;
        margin-bottom: 25px;
    }

    .result-box {
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #dddddd;
        text-align: center;
        margin-top: 15px;
    }

    .result-title {
        font-size: 17px;
        font-weight: 600;
    }

    .result-value {
        font-size: 30px;
        font-weight: 700;
        margin-top: 8px;
    }

    .metric-box {
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #dddddd;
        text-align: center;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# Configuration
# ============================================================

CLASS_NAMES = [
    "glioma",
    "meningioma",
    "notumor",
    "pituitary"
]

MODEL_PATH = "models/best_brain_tumor_resnet18.pth"

DEVICE = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)


# ============================================================
# Image Transform
# ============================================================

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])


# ============================================================
# Load Model
# ============================================================

@st.cache_resource
def load_model():

    model = models.resnet18(weights=None)

    model.fc = nn.Linear(
        model.fc.in_features,
        len(CLASS_NAMES)
    )

    model.load_state_dict(
        torch.load(
            MODEL_PATH,
            map_location=DEVICE
        )
    )

    model = model.to(DEVICE)

    model.eval()

    return model


# ============================================================
# Prediction
# ============================================================

def predict_image(image, model):

    image = image.convert("RGB")

    tensor = transform(image)

    tensor = tensor.unsqueeze(0).to(DEVICE)

    with torch.no_grad():

        output = model(tensor)

        probabilities = torch.softmax(
            output,
            dim=1
        )

        confidence, predicted_class = (
            probabilities.max(dim=1)
        )

    return (
        predicted_class.item(),
        confidence.item(),
        probabilities.cpu().numpy()[0]
    )


# ============================================================
# Grad-CAM
# ============================================================

def generate_gradcam(
    image,
    model,
    predicted_class
):

    image = image.convert("RGB")

    tensor = transform(image)

    tensor = tensor.unsqueeze(0).to(DEVICE)

    target_layer = model.layer4[-1].conv2

    gradcam = GradCAM(
        model=model,
        target_layer=target_layer,
        device=DEVICE
    )

    heatmap, _ = gradcam.generate(
        tensor,
        class_index=predicted_class
    )

    gradcam.remove_hooks()

    original = np.array(image)

    original = cv2.resize(
        original,
        (224, 224)
    )

    heatmap = cv2.resize(
        heatmap,
        (224, 224)
    )

    heatmap_uint8 = np.uint8(
        heatmap * 255
    )

    heatmap_color = cv2.applyColorMap(
        heatmap_uint8,
        cv2.COLORMAP_JET
    )

    heatmap_color = cv2.cvtColor(
        heatmap_color,
        cv2.COLOR_BGR2RGB
    )

    overlay = cv2.addWeighted(
        original,
        0.6,
        heatmap_color,
        0.4,
        0
    )

    return (
        original,
        heatmap,
        overlay
    )


# ============================================================
# Sidebar
# ============================================================

with st.sidebar:

    st.header("🧠 About the Project")

    st.write(
        """
        This application uses a deep learning model to
        classify brain MRI images into four categories.
        """
    )

    st.divider()

    st.subheader("Model")

    st.write("**Architecture:** ResNet18")
    st.write("**Input Size:** 224 × 224")
    st.write("**Classes:** 4")
    st.write("**Test Accuracy:** 94.44%")

    st.divider()

    st.subheader("Classes")

    for class_name in CLASS_NAMES:

        st.write(
            f"• {class_name.capitalize()}"
        )

    st.divider()

    st.caption(
        "Built with PyTorch, Streamlit and Grad-CAM"
    )


# ============================================================
# Main Header
# ============================================================

st.markdown(
    '<div class="main-title">🧠 Brain Tumor MRI Classification</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'ResNet18-based Brain MRI Classification with Explainable AI'
    '</div>',
    unsafe_allow_html=True
)


st.info(
    """
    Upload a brain MRI image to receive a predicted tumor
    class, confidence score and Grad-CAM visualization.
    """
)


# ============================================================
# Model Check
# ============================================================

if not os.path.exists(MODEL_PATH):

    st.error(
        "Model file not found. Please place "
        "`best_brain_tumor_resnet18.pth` inside the "
        "`models` folder."
    )

    st.stop()


model = load_model()


# ============================================================
# Upload Section
# ============================================================

st.subheader("📤 Upload MRI")

uploaded_file = st.file_uploader(
    "Choose a brain MRI image",
    type=["jpg", "jpeg", "png"]
)


# ============================================================
# Prediction
# ============================================================

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    st.image(
        image,
        caption="Uploaded MRI",
        width=450
    )

    st.divider()

    if st.button(
        "🔍 Analyze MRI",
        type="primary",
        use_container_width=True
    ):

        with st.spinner(
            "Analyzing MRI..."
        ):

            predicted_class, confidence, probabilities = (
                predict_image(
                    image,
                    model
                )
            )

            original, heatmap, overlay = (
                generate_gradcam(
                    image,
                    model,
                    predicted_class
                )
            )


        predicted_name = CLASS_NAMES[
            predicted_class
        ]


        # ====================================================
        # Result
        # ====================================================

        st.subheader("🎯 Prediction Result")

        col1, col2 = st.columns(2)

        with col1:

            st.markdown(
                f"""
            <div class="result-box">
    		<div class="result-title">
        	    Predicted Class
    		</div>
    		<div class="result-value">
        	    {predicted_name.upper()}
    		</div>
	    </div>
	    """,
    		unsafe_allow_html=True
	    )
                


        with col2:

            st.markdown(
                f"""
            <div class="result-box">
            	<div class="result-title">
                	Confidence
                </div>

                <div class="result-value">
                    {confidence * 100:.2f}%
                </div>
            </div>
            """,
                unsafe_allow_html=True
            )


        # ====================================================
        # Grad-CAM
        # ====================================================

        st.subheader(
            "🔎 Explainable AI — Grad-CAM"
        )

        st.write(
            """
            Grad-CAM highlights image regions that contributed
            to the model's prediction.
            """
        )

        col1, col2, col3 = st.columns(3)

        with col1:

            st.image(
                original,
                caption="Original MRI",
                use_container_width=True
            )

        with col2:

            st.image(
                heatmap,
                caption="Grad-CAM Heatmap",
                use_container_width=True
            )

        with col3:

            st.image(
                overlay,
                caption="Grad-CAM Overlay",
                use_container_width=True
            )


        # ====================================================
        # Probabilities
        # ====================================================

        st.subheader(
            "📊 Class Probabilities"
        )

        for class_name, probability in zip(
            CLASS_NAMES,
            probabilities
        ):

            st.write(
                f"**{class_name.capitalize()}** — "
                f"{probability * 100:.2f}%"
            )

            st.progress(
                float(probability)
            )


# ============================================================
# Footer / Disclaimer
# ============================================================

st.divider()

st.warning(
    """
    ⚠️ **Research & Educational Use Only**

    This application is not a medical diagnostic system.
    Predictions should not be used as a substitute for
    professional medical evaluation or advice.
    """
)

st.caption(
    "Brain Tumor Classification • ResNet18 • Grad-CAM • PyTorch • Streamlit"
)