# ライブラリのインポート
import cv2
import numpy as np

def filtering(frame,lower,upper):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # HSVによる上限、下限の設定　 ([Hue, Saturation, Value])
    hsvLower = lower
    hsvUpper = upper

    # HSVからマスクを作成
    hsv_mask = cv2.inRange(hsv, hsvLower, hsvUpper)

    # medianblurを用いてノイズ成分を除去
    blur_mask = cv2.medianBlur(hsv_mask, ksize=3)
    return hsv_mask, blur_mask


def labeling(blur_mask,frame):
    # ラベリング結果書き出し用に二値画像をカラー変換 (枠や座標をカラー表示したい！)
    src = frame

    # ラベリング処理
    nlabels, labels, stats, centroids = cv2.connectedComponentsWithStats(blur_mask)

    # 領域(stats[:, 4])が3つ以上ある場合(そのうち1つは背景)だけ処理
    if nlabels >= 3:
        # 面積でソート(今回は面積が上位3つの領域を利用)
        top_idx = stats[:, 4].argsort()[-4:-1]

        # 各領域において...
        for i in top_idx:
            # ターミナル上に詳細表示
            print(
                "[x0: {}, y0: {}, x幅: {}, y幅: {}, 面積: {}]".format(
                    stats[i, 0], stats[i, 1], stats[i, 2], stats[i, 3], stats[i, 4]
                )
            )

            # 領域の外接矩形の角座標を入手
            x, y, w , h, area = stats[i]
            # 長方形描画 (引数 : 描画画像、 長方形の左上角、 長方形の右下角、 色(BGR)、 線の太さ)
            # 長方形以外を使いたい時はURL参照→(http://labs.eecs.tottori-u.ac.jp/sd/Member/oyamada/OpenCV/html/py_tutorials/py_gui/py_drawing_functions/py_drawing_functions.html)
            cv2.circle(src, (x+w//2,y+h//2),(w+h)//4, (0, 0, 255), 5)

            # 領域の重心座標、サイズを表示 (引数 : 描画画像、 書き込む文字列、 書き込む座標、 フォント、 サイズ、 色、 太さ)
            
            x1 = x + w
            y1 = y + h
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
                "Radius: " + str(int((x+y)//4)),
                (x1 - 30, y1 + 45),
                cv2.FONT_HERSHEY_PLAIN,
                1,
                (0, 255, 255),
                2,
            )
            
    return src

def main():
    cap = cv2.VideoCapture(1)

    # 色の範囲
    # HSVRange["blue"]["lower"]で値を取り出せる
    HSVRange = {
        "blue": {"lower": np.array([100, 50, 50]), "upper": np.array([120, 255, 255])},
        "green": {"lower": np.array([35, 80, 80]), "upper": np.array([85, 255, 255])},
        "pink": {"lower": np.array([160, 50, 50]), "upper": np.array([170, 255, 255])},
    }

    # 実行
    while True:
        # -----------以下記述-----------
        ret, frame = cap.read()
        cv2.imshow("camera", frame)
        # circle描画はURL参照→(http://labs.eecs.tottori-u.ac.jp/sd/Member/oyamada/OpenCV/html/py_tutorials/py_gui/py_drawing_functions/py_drawing_functions.html)
        # circle描画の ”引数:線幅” を -1 に設定することで塗り潰しが可能(円の中心点の描画に必要!)

        hsv_mask_pink, blur_mask_pink = filtering(frame,HSVRange["pink"]["lower"],HSVRange["pink"]["upper"])
        hsv_mask_green, blur_mask_green = filtering(frame,HSVRange["green"]["lower"],HSVRange["green"]["upper"])
        hsv_mask_blue, blur_mask_blue = filtering(frame,HSVRange["blue"]["lower"],HSVRange["blue"]["upper"])

        combined_mask = cv2.bitwise_or(blur_mask_green,blur_mask_blue)
        combined_mask = cv2.bitwise_or(blur_mask_pink,combined_mask)

        cv2.imshow("hsv_mask_pink", hsv_mask_pink)
        cv2.imshow("hsv_mask_blue", hsv_mask_blue)
        cv2.imshow("hsv_mask_green", hsv_mask_green)

        cv2.imshow("mask_with_medianblur", combined_mask)
        
        src = labeling(combined_mask,frame)

        # 結果画像の表示
        cv2.imshow("output", src)

        # 終了オプション
        k = cv2.waitKey(1)
        if k == ord("q"):
            break


    # カメラリリース、windowの開放
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
