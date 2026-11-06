import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	a = np.asarray(a)
	if a.size == new_shape[0] * new_shape[1]:
		reshaped_matrix = a.reshape(new_shape).tolist()
	else:
		reshaped_matrix = []
	return reshaped_matrix