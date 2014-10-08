using System;
using System.Linq;

public class RotateMatrixSolution
{
    public static int[][] RotateInPlace(int[][] A, int n)
    {
        // Cyclically permute the entries a layer at a time.
        var first = 0;
        var last = n - 1;
        while (first < last)
        {
            for (var i = 0; i < last - first; i++)
            {
                var temp                = A[    first][first + i];
                A[    first][first + i] = A[ last - i][    first];
                A[ last - i][    first] = A[     last][ last - i];
                A[     last][ last - i] = A[first + i][     last];
                A[first + i][     last] = temp;
            }
            first++;
            last--;
        }

        return A;
    }
    public static int[][] RotateMatrix(int[][] A, int m, int n)
    {
        if (m == n)
        {
            return RotateInPlace(A, n);
        }

        // Initialize an empty n by m matrix.
        var rotated = new int[n][];
        for (var newRow = 0; newRow < n; newRow++)
        {
            rotated[newRow] = new int[m];
        }

        // Copy the elements.
        for (var newRow = 0; newRow < n; newRow++)
        {
            for (var newCol = 0; newCol < m; newCol++)
            {
                rotated[newRow][newCol] = A[m - newCol - 1][newRow];
            }
        }
        return rotated;
    }

    /// <summary>
    /// The entry point.
    /// </summary>
    public static void Main()
    {
        var testMatrices = new[]
        {
            new[]
			{
			    new[] {1, 2},
			    new[] {3, 4}
			},
			new[]
			{
			    new[] {0, 0, 0},
			    new[] {0, 0, 0}
			},
			new[]
			{
			    new[] {1, 2, 3},
			    new[] {4, 5, 6},
                new[] {7, 8, 9}
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
            },
            new[]
            {
                new[] { 1,  2,  3,  4,  5,  6},
                new[] { 7,  8,  9, 10, 11, 12},
                new[] {13, 14, 15, 16, 17, 18},
                new[] {19, 20, 21, 22, 23, 24},
                new[] {25, 26, 27, 28, 29, 30},
                new[] {31, 32, 33, 34, 35, 36}
            }
		};
        var testCase = 1;
        foreach (var A in testMatrices)
        {
            Console.WriteLine("Test Matrix #{0}:", testCase);
            var rotated = RotateMatrix(A, A.Length, A[0].Length);
            Console.WriteLine(string.Join("\n",
                rotated.Select(newRow => "{" + string.Join(", ", newRow) + "}")));
            testCase++;
        }

        Console.Write("\nPress any key to continue...");
        Console.ReadKey();
    }
}