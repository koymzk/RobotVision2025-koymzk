# ライブラリのインポート
import cv2
import numpy as np


def filtering(frame, hsvLower, hsvUpper):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # HSVからマスクを作成
    hsv_mask = cv2.inRange(hsv, hsvLower, hsvUpper)
    # medianblurを用いてノイズ成分を除去
    blur_mask = cv2.medianBlur(hsv_mask, ksize=3)
    return hsv_mask, blur_mask


def labeling(blur_mask, src):
    # ラベリング処理
    nlabels, labels, stats, centroids = cv2.connectedComponentsWithStats(blur_mask)
    # 領域(stats[:, 4])1つ以上ある場合(そのうち1つは背景)だけ処理
    if nlabels >= 1:
        # 面積でソート(今回は面積が上位1つの領域を利用)
        top_idx = stats[:, 4].argsort()[-2:-1]
        # 各領域において...
        for i in top_idx:
            # ターミナル上に詳細表示
            print(
                "[x0: {}, y0: {}, x幅: {}, y幅: {}, 面積: {}]".format(
                    stats[i, 0], stats[i, 1], stats[i, 2], stats[i, 3], stats[i, 4]
                )
            )
            # 領域の外接矩形の角座標を入手
            x0 = stats[i, 0]
            y0 = stats[i, 1]
            x1 = x0 + stats[i, 2]
            y1 = y0 + stats[i, 3]
            gx = int(centroids[i, 0])
            gy = int(centroids[i, 1])
            # cv2.circleの引数はintである必要があるので注意
            cv2.circle(src, (gx, gy), stats[i, 2] // 2, (0, 0, 255), 5)
            cv2.circle(src, (gx, gy), 5, (0, 255, 0), -1)
            # 領域の重心座標、サイズを表示 (引数 : 描画画像、 書き込む文字列、 書き込む座標、 フォント、 サイズ、 色、 太さ)
            cv2.putText(
                src,
                "Center X: " + str(int(centroids[i, 0])),
                (x1 - 30, y1 + 15),
                cv2.FONT_HERSHEY_PLAIN,
                1,
                (0, 255, 255),
                2,
            )
            cv2.putText(
                src,
                "Center Y: " + str(int(centroids[i, 1])),
                (x1 - 30, y1 + 30),
                cv2.FONT_HERSHEY_PLAIN,
                1,
                (0, 255, 255),
                2,
            )
            cv2.putText(
                src,
                "Radius: " + str(int(stats[i, 2] // 2)),
                (x1 - 30, y1 + 45),
                cv2.FONT_HERSHEY_PLAIN,
                1,
                (0, 255, 255),
                2,
            )
    return src


def main():
    cap = cv2.VideoCapture(0)
    # 色の範囲
    # HSVRange["blue"]["lower"]で値を取り出せる
    HSVRange = {
        "blue": {"lower": np.array([100, 50, 50]), "upper": np.array([120, 255, 255])},
        "green": {"lower": np.array([40, 40, 40]), "upper": np.array([60, 255, 255])},
        "pink": {"lower": np.array([160, 50, 50]), "upper": np.array([170, 255, 255])},
    }
    # 実行
    while True:
        # -----------以下記述-----------
        # circle描画はURL参照→(http://labs.eecs.tottori-u.ac.jp/sd/Member/oyamada/OpenCV/html/py_tutorials/py_gui/py_drawing_functions/py_drawing_functions.html)
        # circle描画の ”引数:線幅” を -1 に設定することで塗り潰しが可能(円の中心点の描画に必要!)
        ret, frame = cap.read()
        for color in ["blue", "green", "pink"]:
            _, blur_mask = filtering(frame, HSVRange[color]["lower"], HSVRange[color]["upper"])
            frame = labeling(blur_mask, frame)
        cv2.imshow("output", frame)
        # 終了オプション
        k = cv2.waitKey(1)
        if k == ord("q"):
            break
    # カメラリリース、windowの開放
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()