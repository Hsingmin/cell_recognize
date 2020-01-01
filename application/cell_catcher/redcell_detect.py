
import sys
from yolo import YOLO
from PIL import Image


def detect_img(img):
    # img = input('Input image filename:')
    yolo = YOLO()
    try:
        image = Image.open(img)
    except:
        print("open image failed")
    else:
        res = yolo.detect_image(image)
        labeled_image = res.get_image()
        labeled_image.show()
        print("get bounding boxes: ")
        for box in res.get_boxes():
            print(box)
    yolo.close_session()


if __name__ == '__main__':
    img_name = "BloodImage_00003.jpg"
    detect_img(img_name)
