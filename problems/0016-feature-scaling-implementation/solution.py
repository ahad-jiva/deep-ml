import numpy as np

def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
    standardized_data = np.empty_like(data, dtype=np.float64)
    normalized_data = np.empty_like(data, dtype=np.float64)

    for i in range(data.shape[1]):
        column = data[:, i]
        standard = (column - column.mean()) / (column.std())
        minmax = (column - column.min()) / (column.max() - column.min())
        standardized_data[:, i] = standard
        normalized_data[:, i] = minmax

    return standardized_data.tolist(), normalized_data.tolist()