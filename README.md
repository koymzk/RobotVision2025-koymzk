# Robot Vision 2023

### 講義スライド
- [1週目スライド](https://docs.google.com/presentation/d/1Y1mf8u1hK1CytaBMIGsYJwXy4iI51j-VntDGFAdA-Uk/edit?usp=sharing)
- [2週目スライド](https://docs.google.com/presentation/d/1U1m17uIcqu4qR82MH0CilKQCAR8mdfxrdUiGnr7BdDA/edit?usp=sharing)
- [3週目スライド](https://docs.google.com/presentation/d/1dlsGDZo6LnEL4WmLcqHV7neElv9EAHsdiwAd4sPq6Qo/edit?usp=sharing)

### 講義で使うソースコードのダウンロード
コマンドプロンプト(Power Shell，ターミナル)上で以下のコマンドを実行し，ソースコードをダウンロードできる．
Windowsの場合，ダウンロードしたファイルは `C:\Users\E(ユーザ名))\RobotVision2023` に保存される．
```shell
git clone https://github.com/aoki-media-lab/RobotVision2023.git
```

### faq
- Q. プログラム実行時にエラーが発生する
  - A1. 必要なパッケージがインストールされていない可能性がある．
  `pip install --user -r requirements.txt` と入力し，パッケージをダウンロードする．
  - A2. (自身のPCを使用している場合)ファイルが存在するディレクトリでプログラムを実行する必要がある．
    例えば，first/show_image.pyを実行する場合，firstディレクトリで `python(もしくはpython3) show_image.py` を実行する．
- Q. (Windows) カメラの起動が遅い
  - A. PCによっては `cap = cv2.VideoCapture()` 実行に時間を要する．
  `VideoCapture` の引数に `cv2.CAP_DSHOW` を追加することで解決することができる．
  以下のコマンドを実行してgitのブランチを切り替えることで，ソースコード内の `cv2.VideoCapture(0)` を `cv2.VideoCapture(0, cv2.CAP_DSHOW)` に置き換えることができる．元のブランチに戻す場合は， `git checkout main` を実行する．
```shell
# RobotVisionのディレクトリに移動
cd C:/Users/E/RobotVision2023
# ブランチの切り替え
git checkout patched
```