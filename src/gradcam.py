import torch
import numpy as np


class GradCAM:

    def __init__(self, model, target_layer, device):

        self.model = model
        self.target_layer = target_layer
        self.device = device

        self.activations = None
        self.gradients = None

        # Register hooks
        self.forward_hook = target_layer.register_forward_hook(
            self.save_activations
        )

        self.backward_hook = target_layer.register_full_backward_hook(
            self.save_gradients
        )

    def save_activations(self, module, input, output):

        self.activations = output.detach()

    def save_gradients(self, module, grad_input, grad_output):

        self.gradients = grad_output[0].detach()

    def generate(self, input_tensor, class_index=None):

        self.model.zero_grad()

        # Forward pass
        output = self.model(input_tensor)

        # If class is not specified, use predicted class
        if class_index is None:
            class_index = output.argmax(dim=1).item()

        # Select target class
        target = output[0, class_index]

        # Backward pass
        target.backward()

        # Get gradients and activations
        gradients = self.gradients
        activations = self.activations

        # Global average pooling of gradients
        weights = gradients.mean(
            dim=(2, 3),
            keepdim=True
        )

        # Weighted combination
        cam = (weights * activations).sum(
            dim=1
        )

        # Remove negative values
        cam = torch.relu(cam)

        # Convert to NumPy
        cam = cam.squeeze().cpu().numpy()

        # Normalize between 0 and 1
        cam_min = cam.min()
        cam_max = cam.max()

        if cam_max - cam_min != 0:

            cam = (
                cam - cam_min
            ) / (
                cam_max - cam_min
            )

        else:

            cam = np.zeros_like(cam)

        return cam, class_index

    def remove_hooks(self):

        self.forward_hook.remove()
        self.backward_hook.remove()