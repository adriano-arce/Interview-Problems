def matrix_spiral(A, m, n):
    """
    Prints the contents of the given m by n matrix A by starting from the top
    left corner and spiralling clockwise in towards the centre.
    """
    
    results = []
    
    # These keep track of the corners of the inner submatrix to be printed.
    (row_start, row_stop, col_start, col_stop) = (0, m, 0, n)
    while row_start < row_stop and col_start < col_stop:
        # Print the first row, then the last column.
        for col in range(col_start, col_stop):
            results.append(A[row_start][col])
        for row in range(row_start + 1, row_stop):
            results.append(A[row][col_stop - 1])

        # Check that the current submatrix isn't a narrow row/column.
        if row_stop - row_start > 1 and col_stop - col_start > 1:
            # Print the last row, then the first column.
            for col in range(col_stop - 2, col_start - 1, -1):
                results.append(A[row_stop - 1][col])
            for row in range(row_stop - 2, row_start, -1):
                results.append(A[row][col_start])

        # Move on to the next submatrix.
        row_start += 1
        row_stop -= 1
        col_start += 1
        col_stop -= 1

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
        matrix_spiral(A, len(A), len(A[0]))