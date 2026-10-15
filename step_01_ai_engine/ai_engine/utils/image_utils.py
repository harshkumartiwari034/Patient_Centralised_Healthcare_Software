from PIL import Image

def image_size(path:str):
    img=Image.open(path)
    return img.size
