import numpy as np

def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
    matrix = np.asarray(matrix)
    b = -matrix.trace()
    c = (matrix[0][0] * matrix[1][1]) - (matrix[1][0] * matrix[0][1])
    e1 = (-b + (b**2 - 4 * c)**0.5) / (2)
    e2 = (-b - (b**2 - 4 * c)**0.5) / (2)
    return sorted([e1, e2], reverse=True)