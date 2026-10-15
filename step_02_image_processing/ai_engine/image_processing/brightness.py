import cv2, numpy as np
def brightness_score(image):
    hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    return np.mean(hsv[:,:,2])
def is_too_dark(image,threshold=60):
    s=brightness_score(image)
    return s<threshold,s
