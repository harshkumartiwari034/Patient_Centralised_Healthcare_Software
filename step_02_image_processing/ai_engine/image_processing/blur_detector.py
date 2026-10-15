import cv2
def blur_score(image):
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    return cv2.Laplacian(gray,cv2.CV_64F).var()
def is_blurry(image,threshold=100):
    s=blur_score(image)
    return s<threshold,s
