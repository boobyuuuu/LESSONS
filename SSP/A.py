import numpy as np
import math

sqrt_3 = math.sqrt(3)
sqrt_2 = math.sqrt(2)
sqrt_6 = math.sqrt(6)

# 例如，假设A和T是两个矩阵
A = np.array([[1, 0, 0],
              [0, -1/2, -sqrt_3/2],
              [0, sqrt_3/2, -1/2]])


T = np.array([[1/sqrt_3,0, -2/sqrt_6],
              [1/sqrt_3, 1/sqrt_2, 1/sqrt_6],
              [1/sqrt_3, -1/sqrt_2, 1/sqrt_6]])


# 计算TAT^T
result = np.dot(T, np.dot(A, T.T))


print(A)

print("TAT^T 的结果是：")
print(result)