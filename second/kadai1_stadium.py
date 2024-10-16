# ライブラリのインポート
import copy

import cv2
import numpy as np


def main():
    # アプリ用のスタジアム、ボール画像を読みこみ
    ball_img = cv2.imread("./image_data/ball.png")
    stadium_img = cv2.imread("./image_data/stadium.png")

    # スタジアムの大きさを適当に変更 (二つ目の引数は(w,h)
    stadium_img = cv2.resize(stadium_img, (1200, 700))

    # / ではなく // で切り捨て
    # ボールの高さ、幅の[半分](半分だから注意！！)
    # (注意!)今回ボールの大きさが H:198、W:200と両方偶数のためこれで良いが、奇数の場合は工夫が必要
    ball_h, ball_w = ball_img.shape[0] // 2, ball_img.shape[1] // 2

    # ボールの中心位置（中心座標)を初期ではスタジアムの中心に設定
    idx_h = stadium_img.shape[0] // 2
    idx_w = stadium_img.shape[1] // 2

    print(idx_h)


    while True:
        # スタジアムのコピーを作成
        stadium_copy = copy.deepcopy(stadium_img)

        # ボールの再配置
        stadium_copy[
            (idx_h - ball_h) : (idx_h + ball_h), (idx_w - ball_w) : (idx_w + ball_w)
        ] = ball_img

        # 結果画像の表示
        cv2.imshow("output", stadium_copy)

        # ボールを一回で動かす距離(ピクセル数)を決定
        x = 10

        # 終了オプション
        k = cv2.waitKey(1)
        if k == ord("q"):
            break
        if k == ord("w"):
            idx_h -= x
        elif k == ord("s"):
            idx_h += x
        elif k == ord("a"):
            idx_w -= x
        elif k == ord("d"):
            idx_w += x

        # はみ出す場合は強制的に元の位置に戻す
        # ボールが覆う区間は[idx_h - ball_h, idx_h + ball_h)
        idx_h = min(max(idx_h, ball_h), stadium_copy.shape[0] - ball_h)
        idx_w = min(max(idx_w, ball_w), stadium_copy.shape[1] - ball_w)
        """
        ↑のコードは以下の条件分岐での対処と同じ
        if idx_h - ball_h < 0:
            idx_h = ball_h
        if idx_h + ball_h >= stadium_copy.shape[0]:
            idx_h = stadium_copy.shape[0] - ball_h
        if idx_w - ball_w < 0:
            idx_w = ball_w
        if idx_w + ball_w >= stadium_copy.shape[1]:
            idx_w = stadium_copy.shape[1] - ball_w
        """


    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
