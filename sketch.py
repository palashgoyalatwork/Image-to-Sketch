import cv2
import numpy as np
import scipy.ndimage

def rgb2gray(rgb):
    return np.dot(rgb[..., :3], [0.2989, 0.5870, 0.1140])

def dodge(front, back):
    final_sketch = front * 255 / (255 - back)
    final_sketch[final_sketch > 255] = 255
    final_sketch[back == 255] = 255
    return final_sketch.astype('uint8')

# Ask user for image path
image_path = input("Enter image path: ").strip().replace('"', '')

# Read image
img = cv2.imread(image_path)

if img is None:
    print("Image not found!")
    print("Path entered:", image_path)
    exit()

# Convert BGR to RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Convert to grayscale
gray = rgb2gray(img)

# Invert image
invert = 255 - gray

# Blur image
blur = scipy.ndimage.gaussian_filter(invert, sigma=15)

# Create sketch
sketch = dodge(blur, gray)

# Save sketch
output_file = "sketch.png"
cv2.imwrite(output_file, sketch)

print(f"Sketch saved as {output_file}")

# Show sketch
cv2.imshow("Sketch", sketch)
cv2.waitKey(0)