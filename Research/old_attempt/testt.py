import numpy as np

# Create example matrices
matrix1 = np.array([[1, 2, 3],
                    [4, 5, 6]])

matrix2 = np.array([[7, 8],
                    [9, 10],
                    [11, 12]])

# Calculate the element-wise product
print(matrix1 * matrix2.T)
element_wise_product = np.sum(matrix1 * matrix2.T, axis =1)

print(element_wise_product)
