from pathlib import Path

import cv2
import numpy as np


def load_image(image_path):
    """Load image from file"""
    try:
        # Read image
        image = cv2.imread(str(image_path), cv2.IMREAD_UNCHANGED)

        if image is None:
            print(f"Failed to load image: {image_path}")
            return None

        return image

    except Exception as e:
        print(f"Error loading image {image_path}: {e}")
        return None


def save_edge_map(edge_map, output_path, original_size=None):
    """Save edge detection result"""
    try:
        # Ensure output directory exists
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        # Resize back to original size if needed
        if original_size and (edge_map.shape[1], edge_map.shape[0]) != original_size:
            edge_map = cv2.resize(edge_map, original_size, interpolation=cv2.INTER_LINEAR)

        # Ensure proper format
        if edge_map.dtype != np.uint8:
            edge_map = np.clip(edge_map * 255, 0, 255).astype(np.uint8)

        # Save image
        cv2.imwrite(str(output_path), edge_map)

    except Exception as e:
        print(f"Error saving edge map: {e}")
