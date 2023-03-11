import numpy as np
import cv2
import matplotlib.pyplot as plt


def orig(picture):
    height, width = picture.shape[:2]

    plt.axis('off')
    plt.imshow(picture)
    plt.show()


def translation_1(picture, bx, by, tx, ty):
    height, width = picture.shape[:2]
    
    bx = 0
    by = 0
    nx = bx + tx
    ny = by + ty

    m_translation_ = np.float32([[1,0,nx],
                                 [0,1,ny]])
    translated_img_ = cv2.warpAffine(picture, m_translation_, dsize=(width,height))

    plt.axis('off')
    plt.imshow(translated_img_)
    plt.show()

def main():
    picture = ["quiz1pic1.jpg", "quiz1pic2.jpg", "quiz1pic3.jpg", "quiz1pic4.jpeg", "quiz1pic5.png"]
    bx = int
    by = int
    tx = int(input("How much would you like x to move?:"))
    ty = int(input("How much would you like y to move?:"))

    for p in picture:
        img_ = cv2.imread(f"{p}")
        img_ = cv2.cvtColor(img_, cv2.COLOR_BGR2RGB)
        orig(img_)
        translation_1(img_, bx, by, tx, ty)

main()