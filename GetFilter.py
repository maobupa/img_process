import cv2

img = cv2.imread('image1.jpg')

# scale_factor = 2
# resized = cv2.resize(img, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_LINEAR)
# hsv_resized = cv2.cvtColor(resized, cv2.COLOR_BGR2HSV)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

def show_hsv_on_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        pixel = hsv[y, x]  # Note: OpenCV uses row=y, col=x
        h, s, v = pixel
        print(f"HSV at ({x},{y}): H={h}, S={s}, V={v}")

cv2.namedWindow("Image")
cv2.setMouseCallback("Image", show_hsv_on_click)
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()