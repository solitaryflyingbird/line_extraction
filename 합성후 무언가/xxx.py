import cv2
import numpy as np

def overlay(front, back):
    # Convert front image to 4 channels (RGBA)
    front_rgba = cv2.cvtColor(front, cv2.COLOR_BGR2BGRA)

    # Create an alpha channel for the back image
    back_rgba = np.zeros((back.shape[0], back.shape[1], 4), dtype=np.uint8)
    back_rgba[..., :3] = back
    back_rgba[..., 3] = 255  # Set alpha channel to fully opaque

    # Overlay the front image on the back image
    combined = back_rgba.copy()
    for y in range(front_rgba.shape[0]):
        for x in range(front_rgba.shape[1]):
            alpha_front = front_rgba[y, x, 3] / 255.0
            if alpha_front > 0:  # Only process non-transparent pixels
                combined[y, x, :3] = front_rgba[y, x, :3]
                combined[y, x, 3] = front_rgba[y, x, 3]

    return combined

# Read the images
front = cv2.imread('front.png', cv2.IMREAD_UNCHANGED)
back = cv2.imread('back.png')

# Check if both images have the same size
if front.shape[:2] != back.shape[:2]:
    raise ValueError("Images must have the same size")

# Overlay the front image on the back image
combined = overlay(front, back)

# Save the combined image
cv2.imwrite('combined.png', combined)

# Display the combined image
cv2.imshow('Combined Image', cv2.cvtColor(combined, cv2.COLOR_BGRA2BGR))
cv2.waitKey(0)
cv2.destroyAllWindows()
