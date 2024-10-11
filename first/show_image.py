import cv2


def main(img_path):
    # 画像の読み込み
    img = cv2.imread(img_path)

    # サイズの表示
    print("画像のサイズ:", img.shape)

    # 画像の表示
    cv2.imshow("image", img)

    # 任意のキーを押すと表示を終了
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    img_path = "./keio.png"
    main(img_path)
