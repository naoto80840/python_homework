# 課題1
- Pythonを用いて、一次元熱拡散方程式を、陽解法・陰解法それぞれの方法で解け。
- また、陽解法・陰解法の安定性解析を行い、陽解法の安定性条件と、陰解法が無条件安定であることを示せ。

# 課題2
- Pythonを用いて、一次元の移流方程式を解け。

## 課題1の回答

一次元熱拡散方程式の陽解法

（[1d_diffusion_equation_explicit_method.py](https://github.com/naoto80840/python_homework/blob/master/1d_diffusion_equation_explicit_method.py)の説明）

あらかじめ使用するライブラリをインポートしておく。
```python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
```

時間格子をi、x軸方向の空間格子をjとし、F(i,j)
α = λ * Δt / (Δx * Δx) = 0.5 とすると

```python
F[j+1][i] = F[j][i] + α * (F[j][i+1] - 2 * F[j][i] + F[j][i-1])
```

と表せる。
ただし、

棒の長さ L = Δx * Nx = 100
格子点の数 Nx = 100 個
格子間の距離 Δx = L / Nx = 0.01
時間分割数 Nt = 201 step
計算時間 t_max = 1
1フレームの時間 Δt = 0.005 ※後述の α から逆算
熱拡散率 λ = 0.01

である。

```python
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
```

ここまでで計算の準備が整った。

Fの中身は、

	[[ 20.  20.  20. ... 100. 100. 100.]
	 [ 20.   0.   0. ...   0.   0. 100.]
	 [ 20.   0.   0. ...   0.   0. 100.]
	 ...
	 [ 20.   0.   0. ...   0.   0. 100.]
	 [ 20.   0.   0. ...   0.   0. 100.]
	 [ 20.   0.   0. ...   0.   0. 100.]]

こうなっている。

以下、メインのループ

```python
for j in range(Nt - 1):
	for i in range(Nx - 1):
		# メイン処理
		if i != 0:
			F[j+1][i] = F[j][i] + α * (F[j][i+1] - 2 * F[j][i] + F[j][i-1])


print(F[Nt - 1])
print("計算終了")

```

グラフのアニメーションを描画

```python
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

```
