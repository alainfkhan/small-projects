import numpy as np

def add(A: np.ndarray, B: np.ndarray)-> np.ndarray:
    return np.add(A, B)

def subtract(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    return np.subtract(A, B)

def dot(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    """
    np.dot is dot/matrix product. = A @ B
    np.multiply is element-wise multiplication. = A * B
    
    """
    return np.dot(A,B)


def transpose(A: np.ndarray) -> np.ndarray:
    """
    Similar methods:
    A.transpose()
    A.T 
    """
    return np.transpose(A)

def inverse(A: np.ndarray) -> np.ndarray:
    return np.linalg.inv(A)

def determinant(A: np.ndarray) -> np.ndarray:
    pass

def solve(A: np.ndarray, b: np.ndarray) -> np.ndarray: 
    pass

def trace(A: np.ndarray) -> np.ndarray:
    pass


if __name__ == "__main__":
    A = np.array([[3,1],[2,4]])
    B = np.array([[1,0],[0,1]])
    b = np.array([5,6])
    
    # print(f'A = {A}')
    # print(f'B = {B}')
    # print(f'b = {b}')
    # print(f'A + B = {add(A,B)}')
    # print(f'A - B = {subtract(A,B)}')
    # print(f'A dot B = {dot(A,B)}')
    # print(f'A @ B = {A @ B}')
    # print(f'A transpose = {transpose(A)}')
    # print(f'{A}^(-1) = {inverse(A)}. Such that A*A^(-1) = {dot(A,inverse(A))}')
    
    print(A.transpose())
    