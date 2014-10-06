def zeroOutMatrix(A, m, n):
    """
    Zeroes out each row and column of the given m by n matrix A that
    contains at least one 0.
    """
    
    # Keep track of which rows/cols have at least one 0.
    rowHasZero = [False]*m
    colHasZero = [False]*n

    # Pass 1: Search for zeroes, without modifying A yet.
    for row in range(m):
        for col in range(n):
            if A[row][col] == 0:
                rowHasZero[row] = True
                colHasZero[col] = True

    # Pass 2: Zero out the appropriate rows/cols.
    for row in range(m):
        for col in range(n):
            if rowHasZero[row] or colHasZero[col]:
                A[row][col] = 0

if __name__ == "__main__":
    testMatrices = [
        [[0, 0, 0],
         [0, 0, 0]],
        [[0, 1, 1, 1],
         [1, 2, 3, 4],
         [1, 3, 4, 5]],
        [[1, 0, 1, 8, 0],
         [0, 1, 7, 9, 0],
         [5, 4, 3, 2, 1],
         [6, 0, 2, 3, 2],
         [2, 3, 8, 5, 3],
         [9, 8, 7, 6, 5]],
    ]
    for (index, A) in enumerate(testMatrices):
        zeroOutMatrix(A, len(A), len(A[0]))
        print(str.format("Test Matrix #{0}:", index + 1))
##        print("\n".join(map(lambda row: "[" + ", ".join(map(str, row)) + "]",
##                            A)))
        ############################################
        # Printing a list in Python is really nice.
        ############################################
        print("\n".join(map(str, A)))
        ############################################
