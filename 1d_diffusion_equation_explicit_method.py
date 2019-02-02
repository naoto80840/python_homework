# 一次元熱拡散方程式の陽解法

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 一次元の棒を考える
# この棒の左半分の温度に初期条件 T0 = 20
# 右半分の温度に T0 = 100 が与えられている

# この温度が時間とともに拡散していく様子を
# シミュレーションする
# (つまり温度Tは時間tと位置xの2変数関数)
# T(t, x) と表す。このとき、初期温度は

# T(0, x) = 20 (0 < x < 0.5)
# T(0, x) = 100 (0.5 <= x < 1)

# であり、境界条件は、

# T(t, 0) = 20
# T(t, 1) = 100

# つまりこう

# (T⁰)	    ______
#        |
#   -----
#               (x)

# 〜 Δt秒後 〜

# (T¹)	    ______
#        ／
#   ----
#               (x)


# 棒の長さ L = Δx * Nx = 100
# 格子点の数 Nx = 100 個
# 格子間の距離 Δx = L / Nx = 0.01
# 時間分割数 Nt = 201 step
# 計算時間 t_max = 1
# 1フレームの時間 Δt = 0.005 ※後述の α から逆算
# 熱拡散率 λ = 0.01


#（実装上の関係で）、時間格子をi, x軸方向の空間格子をjとする
# ※時間ステップごとの計算なので時間のネストが浅い方がいい

# T(t, x) を格子で表した、F(i, j)を考える
# α = λ * Δt / (Δx * Δx) = 0.5 とすると

# F(i+1, i) = F(i, j) + α * (F(i, j+1) - 2F(i, j) + F(i, i-j))

# と表せる。

# 格子を生成(境界条件を除く)
Nx = 250
Nt = 10001
F = np.zeros((Nt, Nx - 2))

print("格子と境界条件を生成")

# 境界条件を代入
left = np.full(Nt, 20).reshape(Nt, 1)
right = np.full(Nt, 100).reshape(Nt, 1)

F = np.concatenate((left,F,right), axis=1)

# F(0, i)の値、つまり最初のステップでの格子の状態（初期値）を代入
arr = np.arange(Nx)
F[0] = np.where(arr < 0.5 * Nx, 20, 100)

print("初期値を設定")

# これが0.5より大きいと安定条件を満たさない
α = 0.500

for i in range(Nt - 1):
	for j in range(Nx - 1):
		# メイン処理
		if j != 0:
			F[i+1][j] = F[i][j] + α * (F[i][j+1] - 2 * F[i][j] + F[i][j-1])


print(F[Nt - 1])
print("計算終了")

fig = plt.figure()
ims = []
 
for i in range(Nt):
    if i % 20 == 0: # コマ落とし
	    img = plt.plot(F[i], color="red") # グラフを作成
	    plt.title("1D Diffusion equation")
	    plt.ylim(0,120)
	 
	    ims.append(img) # グラフを配列に追加
 
print("プロット終了")
 
# 100枚のプロットを 1ms ごとに表示するアニメーション
ani = animation.ArtistAnimation(fig, ims, interval=1)
plt.show()