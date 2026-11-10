import numpy as np
def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
	A = np.asarray(A, dtype=np.float64)
	b = np.asarray(b, dtype=np.float64)
	x = np.zeros(b.shape[0], dtype=np.float64)
	for iteration in range(n):
		x_new = np.empty_like(x)
		for i in range(len(x)):
			i_sum = np.float64(0)
			for j in range(len(x)):
				if j != i:
					i_sum += np.float64(A[i][j] * x[j])
			x_new[i] = np.float64((1 / A[i][i]) * (b[i] - i_sum))
		x = x_new
	return [round(x_val, 4) for x_val in x.tolist()]