import numpy as np

# 1: numpy.arrayを用いて任意の2x3の行列を生成し，変数array1に格納せよ．
# reshapeメソッドで2x3に変更
array1 = np.random.randint(0, 10, 6).reshape(2, 3)

# 2: array1の形状を表示せよ．(printを使用)
print(array1.shape)

# 3: numpy.random.randomを用いて配列長100の乱数を生成し，変数array2に格納せよ．
array2 = np.random.random(100)

# 4: スライスを用いて(1-indexedで)11〜20番目の要素を表示せよ．(indexに注意！)
# 11番目の要素のindexは10，そこから10個の要素なので[10, 10 + 10)を見る
print(array2[10:20])

# 5: numpy.sortとスライスを用いて，array2を降順にソートせよ．
# np.sortはソートした配列を返すだけで，元の配列は変えないことに注意
# np.sortは昇順なので，降順に直す
array2 = np.sort(array2)[::-1]

# 6: array2中の各要素の2乗を計算し表示せよ．
# 課題4に合わせて表示する
# 方法は何通りかあるがどれでもOK
array2_squared = array2 * array2    # 要素積で2乗を実現
array2_squared = array2 ** 2        # 要素ごとに2乗
array2_squared = np.pow(array2, 2)  # numpyの冪乗関数
print(array2_squared)
