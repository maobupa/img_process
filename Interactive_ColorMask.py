import cv2
import numpy as np

img = cv2.imread('image1.jpg')

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Callback function that prints slider values
def on_trackbar_change(x):
    h_low = cv2.getTrackbarPos("H low", "Trackbars")
    h_high = cv2.getTrackbarPos("H high", "Trackbars")
    s_low = cv2.getTrackbarPos("S low", "Trackbars")
    s_high = cv2.getTrackbarPos("S high", "Trackbars")
    v_low = cv2.getTrackbarPos("V low", "Trackbars")
    v_high = cv2.getTrackbarPos("V high", "Trackbars")

    print(f"HSV range: lower=({h_low}, {s_low}, {v_low}), upper=({h_high}, {s_high}, {v_high})")

def nothing(x): pass

cv2.namedWindow("Trackbars")
cv2.createTrackbar("H low", "Trackbars", 10, 180, nothing)
cv2.createTrackbar("H high", "Trackbars", 40, 180, nothing)
cv2.createTrackbar("S low", "Trackbars", 60, 255, nothing)
cv2.createTrackbar("S high", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("V low", "Trackbars", 40, 255, nothing)
cv2.createTrackbar("V high", "Trackbars", 180, 255, nothing)

while True:
    h_low = cv2.getTrackbarPos("H low", "Trackbars")
    h_high = cv2.getTrackbarPos("H high", "Trackbars")
    s_low = cv2.getTrackbarPos("S low", "Trackbars")
    s_high = cv2.getTrackbarPos("S high", "Trackbars")
    v_low = cv2.getTrackbarPos("V low", "Trackbars")
    v_high = cv2.getTrackbarPos("V high", "Trackbars")

    lower = np.array([10, s_low, 100])
    upper = np.array([35, s_high, 250])

    mask = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(img, img, mask=mask)
    
    cv2.imshow("Masked", result)
    if cv2.waitKey(1) & 0xFF == 27:  # ESC to quit
        break

cv2.destroyAllWindows()
