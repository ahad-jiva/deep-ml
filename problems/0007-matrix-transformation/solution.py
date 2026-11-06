import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
	A = np.asarray(A)
	T = np.asarray(T)
	S = np.asarray(S)

	detT = np.linalg.det(T)
	detS = np.linalg.det(S)
	if detT == 0 or detS == 0:
		return -1
	invT = np.linalg.inv(T)
	return invT @ A @ S