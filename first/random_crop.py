import cv2
import random

img_path = "./keio.png"

# 画像をランダムに切り取るコードをかく
# 画像は配列として読み込まれるので，
# 画像の切り取りは，配列の一部を取り出せばできる．
def random_crop(img_path):
    # 画像の読み込み
    img = cv2.imread(img_path)
    H, W, _ = img.shape
    size = 128
    # 画像の左上をランダムに指定する
    h = random.randint(0, H - size)
    w = random.randint(0, W - size)
    img_crop = img[h: h + size, w: w + size, :]

    # ステップを1, -1にランダム指定する
    rotate_vertical = (-1) ** (random.randint(0, 1))
    rotate_horizontal = (-1) ** (random.randint(0, 1))
    return img_crop[::rotate_vertical, ::rotate_horizontal, :]


if __name__ == "__main__":
    img_path = "./keio.png"
    random_crop(img_path)
