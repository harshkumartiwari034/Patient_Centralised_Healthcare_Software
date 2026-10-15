import cv2
from .orientation import auto_rotate
from .image_cleaner import clean_image
def preprocess_image(path):
    img=cv2.imread(path)
    if img is None: raise FileNotFoundError(path)
    img=auto_rotate(img)
    img=clean_image(img)
    img=cv2.resize(img,None,fx=2,fy=2)
    return img
