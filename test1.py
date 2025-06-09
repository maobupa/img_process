import cv2
import numpy as np

img = cv2.imread('image1.jpg')
# convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Contrast enhancement: Contrast Limited Adaptive Histogram Equalization (CLAHE)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
enhanced = clahe.apply(gray)

# Gentle Adaptive Thresholding
# Lower 'C' → keeps more faint ink; small block size = finer adaptation
thresh = cv2.adaptiveThreshold(
    enhanced,
    255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY,    # KEEP ink as dark on light bg
    15,                   # block size (odd number)
    5                     # C (lower = more sensitive to light ink)
)
 
# Light Morphological Opening to remove noise
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
# cleaned = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

# Method C: Apply color filter
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define HSV range for the ink
lower = np.array([20, 20, 100])     # brown hue range
upper = np.array([30, 100, 255])  
# Create mask
mask = cv2.inRange(hsv, lower, upper)

# Apply mask to original image
method_c = cv2.bitwise_and(img, img, mask=mask)

# Method D: Binarize + Morph Close
thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                cv2.THRESH_BINARY_INV, 15, 10)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (4, 4))
closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
opened = cv2.morphologyEx(closed, cv2.MORPH_OPEN, kernel)
method_d = cv2.bitwise_not(opened)

# # Optional morphological cleanup
# opened = cv2.morphologyEx(inverted, cv2.MORPH_OPEN, kernel)

# # Median blur
# smoothed = cv2.medianBlur(opened, 3)

# Method A: Canny Edge Detection + Morph Close
edges = cv2.Canny(img, threshold1=50, threshold2=150)
kernel2 = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
closed2 = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel2)
method_a = cv2.bitwise_not(closed2)

cv2.imshow("Original", img)
# cv2.imshow("Suggested", thresh)
# cv2.imshow("CLAHE Enhanced", enhanced)
# cv2.imshow("Thresholded", thresh)
# cv2.imshow("Opened", opened)
cv2.imshow("Method_C", method_c)
cv2.imshow("Method_D", method_d)
cv2.imshow("Method_E", method_a)

cv2.waitKey(0)
cv2.destroyAllWindows()

