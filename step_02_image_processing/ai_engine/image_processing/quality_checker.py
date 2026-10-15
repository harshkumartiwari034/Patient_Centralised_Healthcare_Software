from .preprocessing import preprocess_image
from .blur_detector import is_blurry
from .brightness import is_too_dark
def check_image_quality(path):
    img=preprocess_image(path)
    b,bs=is_blurry(img)
    d,br=is_too_dark(img)
    return {"ok":not(b or d),"blur_score":bs,"brightness":br,"blurry":b,"too_dark":d}
