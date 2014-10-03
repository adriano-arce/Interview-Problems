def matrixSpiral(A, m, n):
    """
    Prints the contents of the given m by n matrix A by starting from the top
    left corner and spiralling clockwise in towards the centre.
    """
    
    results = []
    
    # These keep track of the corners of the inner submatrix to be printed.
    (rowStart, rowStop, colStart, colStop) = (0, m, 0, n)
    while rowStart < rowStop and colStart < colStop:
        # Print the first row, then the last column.
        for col in range(colStart, colStop):
            results.append(A[rowStart][col])
        for row in range(rowStart + 1, rowStop):
            results.append(A[row][colStop - 1])

        # Check that the current submatrix isn't a narrow row/column.
        if rowStop - rowStart > 1 and colStop - colStart > 1:
            # Print the last row, then the first column.
            for col in range(colStop - 2, colStart - 1, -1):
                results.append(A[rowStop - 1][col])
            for row in range(rowStop - 2, rowStart, -1):
                results.append(A[row][colStart])

        # Move on to the next submatrix.
        rowStart += 1
        rowStop -= 1
        colStart += 1
        colStop -= 1

    print(" ".join(map(str, results)))

if __name__ == "__main__":
    testMatrices = [
        [[1],
         [2],
         [3]],
        [[1, 2, 3],
         [6, 5, 4]],
        [[1, 2, 3, 4, 5, 6, 7]],
        [[ 1,  2,  3],
         [10, 11,  4],
         [ 9, 12,  5],
         [ 8,  7,  6]],
        [[ 1,  2,  3,  4,  5],
         [12, 13, 14, 15,  6],
         [11, 10,  9,  8,  7]],
        [[ 1,  2,  3,  4],
         [12, 13, 14,  5],
         [11, 16, 15,  6],
         [10,  9,  8,  7]]
    ]
    for (index, A) in enumerate(testMatrices):
        print(str.format("Test Matrix #{0}:", index + 1))
        matrixSpiral(A, len(A), len(A[0]))
