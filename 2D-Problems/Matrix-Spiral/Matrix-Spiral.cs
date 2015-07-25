using System;
using System.Collections.Generic;

public class MatrixSpiralSolution
{
    public static List<string> MatrixSpiral(int[,] matrix)
    {
        var results = new List<string>();
        // Keep track of the inner submatrix to be processed.
        var row_start = 0;
        var row_stop = matrix.GetLength(0);
        var col_start = 0;
        var col_stop = matrix.GetLength(1);
        while (row_start < row_stop && col_start < col_stop)
        {
            // Print the first row, then the last column.
            for (var col = col_start; col < col_stop; col++)
            {
                results.Add(matrix[row_start, col].ToString());
            }
            for (var row = row_start + 1; row < row_stop; row++)
            {
                results.Add(matrix[row, col_stop - 1].ToString());
            }

            // If the current submatrix isn't a narrow row or column, then
            // print the last row, then the first column.
            if (row_stop - row_start > 1 && col_stop - col_start > 1)
            {
                for (var col = col_stop - 2; col >= col_start; col--)
                {
                    results.Add(matrix[row_stop - 1, col].ToString());
                }
                for (var row = row_stop - 2; row > row_start; row--)
                {
                    results.Add(matrix[row, col_start].ToString());
                }
            }

            // Move on to the next submatrix.
            row_start++;
            row_stop--;
            col_start++;
            col_stop--;
        }
        return results;
    }

    /// <summary>
    /// The entry point.
    /// </summary>
    public static void Main()
    {
        var testMatrices = new[]
        {
            new[,] 
            {
                {1},
                {2},
                {3}
            },
            new[,] 
            {
                {1, 2, 3},
                {6, 5, 4}
            },
            new[,]
            {
                {1, 2, 3, 4, 5, 6, 7}
            },
            new[,]
            {
                {1, 2, 3},
                {10, 11, 4}, 
                {9, 12, 5},
                {8, 7, 6}
            },
            new[,] 
            {
                {1, 2, 3, 4, 5}, 
                {12, 13, 14, 15, 6},
                {11, 10, 9, 8, 7}
            },
            new[,]
            {
                {1, 2, 3, 4},
                {12, 13, 14, 5},
                {11, 16, 15, 6},
                {10, 9, 8, 7}
            }
        };
        for (var i = 0; i < testMatrices.Length; i++)
        {
            Console.WriteLine("Test Matrix #{0}:", i + 1);
            var result = MatrixSpiral(testMatrices[i]);
            Console.WriteLine("    " + string.Join(", ", result));
        }
    }
}