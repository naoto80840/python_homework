import numpy as np

# A = np.array([[1., 2., 4.], [3., 4., 8.], [-1., 4., 2.]])
# b = np.array([7., 15., 5.])

# # これは、
# # (1 2 4)  (x) (7)
# # (3 4 8)  (y) (15)
# # (-1 4 2) (z) (5)

# # Ax = b

# # という連立方程式を解いて (x, y ,z) を求めるということ

# for i in range(len(A)-1): # 左下をゼロにする
# 	for j in range(i+1, len(A)):
# 		coef = A[j][i] / A[i][i]
# 		A[j] -= A[i] * coef
# 		b[j] -= b[i] * coef

# for i in range(len(A)-1, 0, -1): # 右上をゼロにする
# 	b[i] /= A[i][i]
# 	A[i] /= A[i][i]
# 	for j in range(i):
# 		b[j] -= b[i] * A[j][i]
# 		A[j][i] = 0


# # A は単位行列になっている
# print(b) #Solution

step = 3
Nx = 4

F = [[20, 0 , 0 , 0, 100], [20, 0, 0, 0, 100],[20, 0, 0, 0, 100]]


for i in range(Nt-1):
	r = np.zeros(Nx-1)
	while True:
		for j in range(Nx-1):
			pre = F[i+1][j+1]
			F[i+1][j+1] = (1 / 3) * (F[i+1][j] + F[i+1][j+2] + F[i][j+1])
			r[j] = F[i+1][j+1] - pre

		if np.max(r) < 1e-15:
			break
print(F)



