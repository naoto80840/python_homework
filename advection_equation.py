import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
import matplotlib.animation as animation

n = np.linspace(-5.0, 5.0, 10000)

Nx = 201
Nt = 501
L = 1 # スケール
v = 1 # 速度
Δx = L / (Nx - 1)
print(Δx)
Δt = 0.2 * Δx
print(Δt/Δx)
F = np.zeros((Nt, Nx - 2))

print("格子と境界条件を生成")

# 境界条件を代入
left = np.full(Nt, 0).reshape(Nt, 1)
right = np.full(Nt, 0).reshape(Nt, 1)

F = np.concatenate((left,F,right), axis=1)

# F(0, i)の値、つまり最初のステップでの格子の状態（初期値）を代入

x = np.arange(Nx)
F[0] = 1000 * norm.pdf(x, loc=50, scale=16)

print("初期値を設定")

for i in range(Nt - 1):
	for j in range(1, Nx - 2):
		# メイン処理
		F[i+1][j] = F[i][j] - Δt * ((-F[i][j+2] + 8 * F[i][j+1] - 8 * F[i][j-1] + F[i][j-2]) / (12 * Δx) + ((F[i][j+2] - 4 * F[i][j+1] + 6 * F[i][j] - 4 * F[i][j-1] + F[i][j-2]) / (4 * Δx)))


fig = plt.figure()
ims = []
 
for i in range(Nt):
    if True: # コマ落とし
	    img = plt.plot(F[i], color="red") # グラフを作成
	    plt.title("1D Diffusion equation")
	    plt.ylim(0,60)
	 
	    ims.append(img) # グラフを配列に追加
 
print("プロット終了")
 
# 100枚のプロットを 1ms ごとに表示するアニメーション
ani = animation.ArtistAnimation(fig, ims, interval=1)
plt.show()