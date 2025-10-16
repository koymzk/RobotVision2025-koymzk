# ライブラリのインポート
import cv2
import numpy as np

# -----------以下記述-----------
# ライブラリのインポート
import numpy as np
import cv2

caps = [cv2.VideoCapture(0), cv2.VideoCapture(1)]
grayscale = False
flip = False
pause = False

# 実行
while(True):
    for cap in caps:
        if not cap.isOpened():  # カメラが開けない場合
            print("カメラが開けません")
            continue
        if not pause:
            ret, frame = cap.read()
            if not ret:  # フレームが正しく取得できていない場合
                print("フレームの読み込みに失敗しました")
                continue
        if grayscale:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if flip:
            frame = cv2.flip(frame,1)
        cv2.imshow('camera',frame)
    
    # 終了オプション
    k = cv2.waitKey(1)
    if k == ord('q'):
        break
    elif k == ord('g'):
        grayscale = not grayscale
    elif k == ord('f'):
        flip = not flip
    elif k == ord('p'):
        pause = not pause

for cap in caps:
    cap.release()
cv2.destroyAllWindows()
