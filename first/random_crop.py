import cv2
import numpy as np

img_path = "./keio.png"
# 画像をランダムに切り取るコードをかく
# 画像は配列として読み込まれるので，
# 画像の切り取りは，配列の一部を取り出せばできる．
def random_crop(img_path):
    # 画像の読み込み
    img = cv2.imread(img_path)
    pass


if __name__ == "__main__":
    img_path = "./keio.png"
    random_crop(img_path)
