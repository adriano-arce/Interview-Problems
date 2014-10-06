using System;
using System.Linq;

public class ZeroOutMatrixSolution
{
    /// <summary>
    /// Given an m by n matrix A, zeroes out each row and column that contains a 0.
    /// </summary>
    /// <param name="A">The matrix to be zeroed out.</param>
    /// <param name="m">The number of rows in A.</param>
    /// <param name="n">The number of columns in A.</param>
    public static void ZeroOutMatrix(int[][] A, int m, int n)
    {
        // Keep track of which rows/cols have at least one 0. Initially false.
        var rowHasZero = new bool[m];
        var colHasZero = new bool[n];

        // Pass 1: Search for zeroes, without modifying A yet.
        for (var row = 0; row < m; row++)
        {
            for (var col = 0; col < n; col++)
            {
                if (A[row][col] == 0)
                {
                    rowHasZero[row] = true;
                    colHasZero[col] = true;
                }
            }
        }

        // Pass 2: Zero out the appropriate rows/cols.
        for (var row = 0; row < m; row++)
        {
            for (var col = 0; col < n; col++)
            {
                if (rowHasZero[row] || colHasZero[col])
                {
                    A[row][col] = 0;
                }
            }
        }
    }

    /// <summary>
    /// The entry point.
    /// </summary>
    public static void Main()
    {
        var testMatrices = new[] {
			new[]
			{
			    new[] {0, 0, 0},
			    new[] {0, 0, 0}
			},
            new[]
            {
                new[] {0, 1, 1, 1},
                new[] {1, 2, 3, 4},
                new[] {1, 3, 4, 5}
            },
            new[]
            {
                new[] {1, 0, 1, 8, 0},
                new[] {0, 1, 7, 9, 0},
                new[] {5, 4, 3, 2, 1},
                new[] {6, 0, 2, 3, 2},
                new[] {2, 3, 8, 5, 3},
                new[] {9, 8, 7, 6, 5}
            }
		};
        var testCase = 1;
        foreach (var A in testMatrices)
        {
            Console.WriteLine("Test Matrix #{0}:", testCase);
            ZeroOutMatrix(A, A.Length, A[0].Length);
            Console.WriteLine(string.Join("\n", A.Select(row => "{" + string.Join(", ", row.Select(num => num.ToString())) + "}")));
            testCase++;
        }

        Console.Write("\nPress any key to continue...");
        Console.ReadKey();
    }
}