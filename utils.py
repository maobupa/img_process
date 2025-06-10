import cv2
import numpy as np
import os 

img = cv2.imread('image3.jpg')
# convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def clahe_enhance(image: np.ndarray) -> np.ndarray:
    """
    This method is suggested by GPT
    CLAHE + adaptive thresholding + morphological opening
    """
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Create a CLAHE object (Arguments are optional)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    # Apply the CLAHE to the grayscale image
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
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
    cleaned = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

    return cleaned

def method_c(image: np.ndarray) -> np.ndarray:
    """
    This method applies a color filter to isolate brown ink
    """
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define HSV range for the ink
    lower = np.array([20, 20, 100])     # brown hue range
    upper = np.array([30, 100, 255])  
    # Create mask
    mask = cv2.inRange(hsv, lower, upper)

    # Apply mask to original image
    filtered_image = cv2.bitwise_and(image, image, mask=mask)

    return filtered_image

def method_d(image: np.ndarray) -> np.ndarray:
    """
    This method applies adaptive thresholding, morphological closing, and opening
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                    cv2.THRESH_BINARY_INV, 15, 10)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (4, 4))
    closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
    opened = cv2.morphologyEx(closed, cv2.MORPH_OPEN, kernel)
    
    return cv2.bitwise_not(opened)

def method_d_stronger(image: np.ndarray) -> np.ndarray:
    """
    This method applies adaptive thresholding, morphological closing, and opening
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                    cv2.THRESH_BINARY_INV, 21, 12)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (4, 4))
    closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
    opened = cv2.morphologyEx(closed, cv2.MORPH_OPEN, kernel)
    
    return cv2.bitwise_not(opened)

def method_d_mean(image: np.ndarray) -> np.ndarray:
    """
    This method applies adaptive thresholding, morphological closing, and opening
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, 
                                    cv2.THRESH_BINARY_INV, 21, 12)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (4, 4))
    closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
    opened = cv2.morphologyEx(closed, cv2.MORPH_OPEN, kernel)
    
    return cv2.bitwise_not(opened)

def method_a(image: np.ndarray) -> np.ndarray:
    """
    This method applies Canny edge detection followed by morphological closing
    """
    edges = cv2.Canny(image, threshold1=50, threshold2=150)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    closed = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)
    
    return cv2.bitwise_not(closed)

img = cv2.imread('image3.jpg')
test1 = method_d(img)
test2 = method_d_stronger(img)
test3 = method_d_mean(img)

# cv2.imshow("Original", img)
# cv2.imshow("Suggested", thresh)
# cv2.imshow("CLAHE Enhanced", enhanced)
# cv2.imshow("Thresholded", thresh)
# cv2.imshow("Opened", opened)
# cv2.imshow("Method_C", method_c)
cv2.imshow("Method_D", test1)
cv2.imshow("Method_D_Stronger", test2)
cv2.imshow("Method_D_Mean", test3)
# cv2.imshow("Method_A", method_a)

cv2.waitKey(0)
cv2.destroyAllWindows()

