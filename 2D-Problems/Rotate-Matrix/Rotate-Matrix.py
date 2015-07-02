def rotate_matrix(A, m, n):
    """
    Rotates the given m by n matrix A 90 degrees clockwise.
    """
    B = [[0] * m for i in range(n)]
    for i in range(m):
        for j in range(n):
            B[j][m - i - 1] = A[i][j]
    return B

if __name__ == "__main__":
    testMatrices = [
        [[0, 0, 0],
         [0, 0, 0]],
        [[0, 1, 1, 1],
         [1, 2, 3, 4],
         [1, 3, 4, 5]],
        [[0, 1, 1, 1],
         [1, 2, 3, 4],
         [1, 3, 4, 5],
         [1, 4, 5, 6]],
        [[1, 0, 1, 8, 0],
         [0, 1, 7, 9, 0],
         [5, 4, 3, 2, 1],
         [6, 0, 2, 3, 2],
         [2, 3, 8, 5, 3],
         [9, 8, 7, 6, 5]],
    ]
    for (index, A) in enumerate(testMatrices):
        B = rotate_matrix(A, len(A), len(A[0]))
        print("Test Matrix #{}:".format(index + 1))
        print("\n".join(map(str, B)))