import cv2
from utils import method_a, method_c, method_d, clahe_enhance, method_d_mean, method_d_stronger
import os

# Before running this script, ensure you have the required directories:
# - 'originals' containing the input images
# - 'output' where the processed images will be saved
# Uncomment the methods you want to use by removing the '#' before the method calls.

# get paths to all the images
folder_path = 'originals'
images_path = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.jpg')]

for image_path in images_path:
    img = cv2.imread(image_path)
    
    # Method A: Canny Edge Detection + Morph Close
    # method_a_result = method_a(img)
    # cv2.imwrite(os.path.join('output', f'method_a_{os.path.basename(image_path)}'), method_a_result)

    # Method C: Apply color filter
    # method_c_result = method_c(img)
    # cv2.imwrite(os.path.join('output', f'method_c_{os.path.basename(image_path)}'), method_c_result)

    # Method D: Binarize + Morph Close + Morph Open
    method_d_result = method_d(img)
    cv2.imwrite(os.path.join('output', f'method_d_{os.path.basename(image_path)}'), method_d_result)

    # Method D Stronger: Binarize + Morph Close + Morph Open
    method_d_stronger_result = method_d_stronger(img)
    cv2.imwrite(os.path.join('output', f'method_d_stronger_{os.path.basename(image_path)}'), method_d_stronger_result)
    # Method D Mean: Binarize + Morph Close + Morph Open
    method_d_mean_result = method_d_mean(img)
    cv2.imwrite(os.path.join('output', f'method_d_mean_{os.path.basename(image_path)}'), method_d_mean_result)

    # CLAHE enhancement
    # clahe_result = clahe_enhance(img)
    # cv2.imwrite(os.path.join('output', f'clahe_{os.path.basename(image_path)}'), clahe_result)
