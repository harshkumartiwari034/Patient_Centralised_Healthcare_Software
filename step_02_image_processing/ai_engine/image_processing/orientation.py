import cv2
def auto_rotate(image):
    h,w=image.shape[:2]
    return cv2.rotate(image,cv2.ROTATE_90_CLOCKWISE) if h>w else image
