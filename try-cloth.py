import numpy as np
import cv2
from tkinter import filedialog
import pdb
pdb.set_trace()
cap = cv2.VideoCapture(0)
img_picked = ""
img_path = filedialog.askopenfile(initialdir=r'clothes')
img_picked = img_path.name
img_path.close()

if not (cap.isOpened()):
    print("No camera found")

while (True):
    # capture frame by frame
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    print("hsv value", hsv)
    lower_shade = np.array([25, 52, 72])
    upper_shade = np.array([102, 255, 255])
    mask_white = cv2.inRange(hsv, lower_shade, upper_shade)
    mask_black = cv2.bitwise_not(mask_white)
    blurred_frame = cv2.GaussianBlur(frame, (25, 25), 0)
    W, L = mask_black.shape
    mask_black_3d = np.empty((W, L, 3), dtype=np.uint8)
    mask_black_3d[:, :, 0] = mask_black
    mask_black_3d[:, :, 1] = mask_black
    mask_black_3d[:, :, 2] = mask_black

    dist = cv2.bitwise_and(mask_black_3d, frame)
    W, L = mask_white.shape
    mask_white_3d = np.empty((W, L, 3), dtype=np.uint8)
    mask_white_3d[:, :, 0] = mask_white
    mask_white_3d[:, :, 1] = mask_white
    mask_white_3d[:, :, 2] = mask_white

    # cv2.imshow('white', mask_white_3d)
    dist_wh = cv2.bitwise_or(mask_white_3d, dist)

    design = cv2.imread(img_path.name)
    design = cv2.resize(design, mask_black.shape[1::-1])

    design_mask_mixed = cv2.bitwise_or(mask_black_3d, design)
    final_mask_black = cv2.bitwise_and(design_mask_mixed, dist_wh)
    cv2.imshow('final', final_mask_black)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
