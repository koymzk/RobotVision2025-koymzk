"""
OpenCVを用いたオプティカルフロー
参考ページ : http://labs.eecs.tottori-u.ac.jp/sd/Member/oyamada/OpenCV/html/py_tutorials/py_video/py_lucas_kanade/py_lucas_kanade.html
"""

# ライブラリのインポート
import time

import cv2
import numpy as np


"""
コーナー検出器のパラメータ設定
"""

# Shi-Tomasiのコーナー検出パラメータ
feature_params = dict(
    maxCorners=100,  # 保持するコーナー数, int
    qualityLevel=0.3,  # 最良値(最大固有値の割合?), float型
    minDistance=7,  # この距離内のコーナーを棄却, float型
    blockSize=7,
)  # 使用する近傍領域のサイズ, int

# Lucas-Kanade法のパラメータ
lk_params = dict(
    winSize=(15, 15),  # 検索ウィンドウのサイズ
    maxLevel=2,  # 検出器の構造を決める(そのままで良い)
    criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03),
)  # 検索終了条件

# ランダムに色を１００個生成（値0～255の範囲で100行3列のランダムなndarrayを生成）
color = np.random.randint(0, 255, (100, 3))


def detect_flow(frame, gray, feature, flow_mask):
    # グレースケールに変換
    gray_next = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # オプティカルフロー検出
    # feature_next : gray_nextの特徴点の座標を保持
    feature_next, status, err = cv2.calcOpticalFlowPyrLK(
        gray, gray_next, feature, None, **lk_params
    )

    # 特徴点の移動を検出できた場合
    if feature_next is not None:
        # オプティカルフローを検出した特徴点を選別（0：検出せず、1：検出した）
        good_first = feature[status == 1]
        good_next = feature_next[status == 1]

    # オプティカルフローを描画
    for i, (next_point, first_point) in enumerate(zip(good_next, good_first)):
        # 前フレームの座標獲得
        first_x, first_y = map(int, first_point.ravel())

        # 後フレームの座標獲得
        next_x, next_y = map(int, next_point.ravel())

        # 前フレームと後フレームを繋ぐ線を描画
        print(flow_mask.shape, (next_x, next_y), (first_x, first_y))
        flow_mask = cv2.line(
            flow_mask, (next_x, next_y), (first_x, first_y), color[i].tolist(), 2
        )

        # 現在の特徴点のところに丸（大きな点）を描画
        frame = cv2.circle(frame, (next_x, next_y), 5, color[i].tolist(), -1)

    return frame, gray_next, good_next


def main():
    # 今回はサンプル動画(.avi形式)を用いてオプティカルフローを観測
    cap = cv2.VideoCapture("./image_data/opticalflow.avi")

    """
    最初のフレームの処理
    Webカメラを用いる場合は、キーボード操作とかで最初のフレームを指定しても良い
    """

    # 最初のフレーム読み込み
    first_flag, first = cap.read()

    # グレースケールに変換
    gray = cv2.cvtColor(first, cv2.COLOR_BGR2GRAY)
    feature = cv2.goodFeaturesToTrack(gray, mask=None, **feature_params)

    # フロー書き出し用の画像作成
    flow_mask = np.zeros_like(first)

    """
    ２枚目以降の処理
    """
    while True:
        # 動画のフレーム取得
        ret, frame = cap.read()

        # 動画のフレームが無くなったら強制終了
        if not ret:
            break

        frame, gray_next, feature_next = detect_flow(frame, gray, feature, flow_mask)

        output = cv2.add(frame, flow_mask)

        # ウィンドウに結果を表示
        cv2.imshow("window", output)

        # 終了オプション
        k = cv2.waitKey(1)
        if k == ord("q"):
            break

        # 次のフレーム、ポイントの準備
        gray = gray_next.copy()
        feature = feature_next.reshape(-1, 1, 2)

        # 動画が早すぎるので0.05秒停止
        time.sleep(0.05)

    # 終了処理
    cv2.destroyAllWindows()
    cap.release()


if __name__ == "__main__":
    main()
