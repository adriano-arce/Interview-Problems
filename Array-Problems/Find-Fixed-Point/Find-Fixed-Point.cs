using System;

public class FindFixedPointSolution
{
    /// <summary>
    /// Returns i such that arr[i] = i (or -1, if no such i exists).
    /// </summary>
    /// <param name="arr">The array to be scanned.</param>
    /// <returns>The first fixed point, if it exists.</returns>
    public static int FindFixedPoint(int[] arr)
    {
        return -1;
    }

    /// <summary>
    /// The entry point.
    /// </summary>
    public static void Main()
    {
        var testArrs = new[] 
        {
            new int[] {},
            new[] {-1, 1},
            new[] {-3, -2, 0, 5, 6, 7},
            new[] {-3, -1, 1, 3, 5, 6},
            new[] {0, 2, 3, 4, 5, 6, 7, 8, 9},
            new[] {-1, 2, 3, 4, 4, 4, 5, 7, 8},
            new[] {-2, -2, 1, 3, 4, 5, 5, 6, 8},
            new[] {-3, -2, 1, 1, 2, 4, 7, 9, 10}
        };
        for (var i = 0; i < testArrs.Length; i++)
        {
            Console.WriteLine("Test Case #{0}: [{1}]", i + 1, string.Join(", ", testArrs[i]));
            Console.WriteLine("    Fixed Point: {0}", FindFixedPoint(testArrs[i]));
        }
    }
}