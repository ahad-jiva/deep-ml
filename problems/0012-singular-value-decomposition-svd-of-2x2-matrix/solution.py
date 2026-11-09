import numpy as np

def svd_2x2_singular_values(A: np.ndarray) -> tuple:
    """
    Compute SVD of a 2x2 matrix using one Jacobi rotation.
    
    Args:
        A: A 2x2 numpy array
    
    Returns:
        Tuple (U, S, Vt) where A ≈ U @ diag(S) @ Vt
        - U: 2x2 orthogonal matrix
        - S: length-2 array of singular values
        - Vt: 2x2 orthogonal matrix (transpose of V)
    """
    ata = np.array([
        [A[0][0]**2 + A[1][0]**2, A[0][0]*A[0][1] + A[1][0]*A[1][1]],
        [A[0][0]*A[0][1] + A[1][0]*A[1][1], A[0][1]**2 + A[1][1]**2]
        ])

    if ata[0][0] == ata[1][1]:
        theta = np.pi / 4
    else:
        theta = 0.5 * np.atan((2 * ata[0][1]) / (ata[0][0] - ata[1][1]))
    
    r_theta = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta), np.cos(theta)]
    ])

    D = r_theta.T @ ata @ r_theta
    singular_values = np.diag(D)**0.5

    V = r_theta
    U = A @ V @ np.diag(1 / singular_values)

    return (U, np.sort(singular_values, descending=True), V.T)
