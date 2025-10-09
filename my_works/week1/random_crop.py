import cv2
import numpy as np


# 画像をランダムに切り取るコードをかく
# 画像は配列として読み込まれるので，
# 画像の切り取りは，配列の一部を取り出せばできる．
def random_crop(img_path):
    # 画像の読み込み
    img = cv2.imread(img_path)
    h, w, _ = img.shape
    x = np.random.randint(0, w - 128 + 1)
    y = np.random.randint(0, h - 128 + 1)
    output = img[y:y+128:np.random.choice([-1,1]), x:x+128:np.random.choice([-1,1])]
    return output


if __name__ == "__main__":
    img_path = "my_works/week1/keio.png"
    random_crop(img_path)
