# ライブラリのインポート
import cv2
import numpy as np


def main():
    cap = cv2.VideoCapture(0)
    grayscale = False
    flip = False
    stop = False

    while True:
        if not stop:
            ret, frame = cap.read()
            if grayscale:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            if flip:
                frame = frame[:, ::-1]
        cv2.imshow("camera", frame)
        k = cv2.waitKey(1)
        if k == ord("q"):
            break
        if k == ord("g"):
            grayscale ^= True
        elif k == ord("f"):
            flip ^= True
        elif k == ord("s"):
            stop ^= True


if __name__ == "__main__":
    main()
