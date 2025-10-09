import cv2
import random_crop


def main(img_path):
    # 画像の読み込み
    img = random_crop.random_crop(img_path)

    # サイズの表示
    print("画像のサイズ:", img.shape)

    # 画像の表示
    cv2.imshow("image", img)

    # 任意のキーを押すと表示を終了
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    img_path = "my_works/week1/keio.png"
    main(img_path)
