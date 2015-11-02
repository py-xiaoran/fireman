from PIL import Image

def AnalyImg(img_path):
    img =  Image.open(img_path)
    info = dict()
    if img:
        info['weight'] = img.size[0]
        info['height'] = img.size[1]
        info['mode']  = img.mode
    return info
