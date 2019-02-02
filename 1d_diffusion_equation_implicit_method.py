import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

Nx = 100
Nt = 501
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


# 棒の長さ L = Δx * Nx = 100
# 格子点の数 Nx = 100 個
# 格子間の距離 Δx = L / Nx = 0.01
# 時間分割数 Nt = 201 step
# 計算時間 t_max = 1
# 1フレームの時間 Δt = 0.005 ※後述の α から逆算
# 熱拡散率 λ = 0.01

# ω = 1, α = 1

for i in range(Nt-1):
	r = np.zeros(Nx-1) # 残差を初期化
	while True:
		for j in range(Nx-2):
			pre = F[i+1][j+1]
			F[i+1][j+1] = (1 / 3) * (F[i+1][j] + F[i+1][j+2] + F[i][j+1])
			r[j] = F[i+1][j+1] - pre

		if np.max(r) < 1e-15:
			break

fig = plt.figure()
ims = []
 
for i in range(Nt):
    # if i % 20 == 0: # コマ落とし
    img = plt.plot(F[i], color="red") # グラフを作成
    plt.title("1D Diffusion equation")
    plt.ylim(0,120)
 
    ims.append(img) # グラフを配列に追加
 
print("プロット終了")
 
# 100枚のプロットを 1ms ごとに表示するアニメーション
ani = animation.ArtistAnimation(fig, ims, interval=1)
plt.show()