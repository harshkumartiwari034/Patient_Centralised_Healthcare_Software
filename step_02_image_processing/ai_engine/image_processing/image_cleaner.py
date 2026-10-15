import cv2
def clean_image(image):
    g=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    d=cv2.fastNlMeansDenoising(g)
    return cv2.cvtColor(d,cv2.COLOR_GRAY2BGR)
