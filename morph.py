from __future__ import print_function
import cv2 as cv
import numpy as np
import argparse
import sys

morph_size = 0
max_operator = 4
max_elem = 2
max_kernel_size = 21
title_trackbar_operator_type = 'Operator:\n 0: Opening - 1: Closing  \n 2: Gradient - 3: Top Hat \n 4: Black Hat'
title_trackbar_element_type = 'Element:\n 0: Rect - 1: Cross - 2: Ellipse'
title_trackbar_kernel_size = 'Kernel size:\n 2n + 1'
title_window = 'Morphology Transformations Demo'
morph_op_dic = {
    0: cv.MORPH_OPEN,
    1: cv.MORPH_CLOSE,
    2: cv.MORPH_GRADIENT,
    3: cv.MORPH_TOPHAT,
    4: cv.MORPH_BLACKHAT
}

def morphology_operations(val):
    morph_operator = cv.getTrackbarPos(title_trackbar_operator_type, title_window)
    morph_size = cv.getTrackbarPos(title_trackbar_kernel_size, title_window)
    val_type = cv.getTrackbarPos(title_trackbar_element_type, title_window)

    operations = ["Opening", "Closing", "Gradient", "Top Hat", "Black Hat"]
    # print(f"Selected operation: {operations[morph_operator]}\n")
    # print(f"Selected morph size: {morph_size}")
    # print(f"Selected value type: {val_type}")

    morph_elem = cv.MORPH_RECT if val_type == 0 else cv.MORPH_CROSS if val_type == 1 else cv.MORPH_ELLIPSE
    ksize = 2 * morph_size + 1

    # print(f"[DEBUG] morph_size = {morph_size}, ksize = {ksize}")
    try:
        element = cv.getStructuringElement(morph_elem, (ksize, ksize))
        operation = morph_op_dic[morph_operator]
        dst = cv.morphologyEx(src, operation, element)
        cv.imshow(title_window, dst)
    except cv.error as e:
        print(f"[ERROR] OpenCV error during operation: {e}")

if __name__ == "__main__":
    try:
        # Clear Jupyter args if needed
        import sys
        if "ipykernel" in sys.modules:
            sys.argv = ['']

        parser = argparse.ArgumentParser(description='Code for Morphology Transformations.')
        parser.add_argument('--input', help='Path to input image.', default='LinuxLogo.jpg')
        args = parser.parse_args()

        global src
        src = cv.imread(cv.samples.findFile(args.input))
        if src is None:
            print('Could not open or find the image:', args.input)
            sys.exit(1)

        cv.namedWindow(title_window)
        cv.createTrackbar(title_trackbar_operator_type, title_window, 0, max_operator, morphology_operations)
        cv.createTrackbar(title_trackbar_element_type, title_window, 0, max_elem, morphology_operations)
        cv.createTrackbar(title_trackbar_kernel_size, title_window, 1, max_kernel_size, morphology_operations)

        morphology_operations(0)
        print("Press any key in the OpenCV window to exit...")
        cv.waitKey(0)

    except KeyboardInterrupt:
        print("\n[INFO] Interrupted by user. Exiting cleanly...")
        cv.destroyAllWindows()
        sys.exit(0)
