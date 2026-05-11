import numpy as np

# Input matrices
print("Enter Matrix A:")
matrix_a = np.array([list(map(int, input().split())) for i in range(3)])

print("Enter Matrix B:")
matrix_b = np.array([list(map(int, input().split())) for i in range(3)])

Addition = np.add(matrix_a,matrix_b)
# Addition
print("Addition (A + B):")
print(Addition)
Sub = np.subtract(matrix_a,matrix_b)
# Subtraction
print("Subtraction (A - B):")
print(Sub)
multy = np.multiply(matrix_a,matrix_b)
# Multiplication (element-wise)
print("Element-wise Multiplication (A * B):")
print(multy)
dota = np.dot(matrix_a,matrix_b)
# Matrix multiplication (dot product)
print("A dot B:")
print(dota)
f = matrix_a.T
# Transpose
print("Transpose of A:")
print(f)
