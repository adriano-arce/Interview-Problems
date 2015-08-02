using System;

public class FindEquilibriumSolution
{
    /// <summary>
    /// The entry point.
    /// </summary>
    public static void Main()
    {
        var testArrs = new[] 
        {
            new int[] {},
            new[] {-7, 1, 5, 2, -4, 3, 0},
            new[] {1, 2, 3, 4, 5},
            new[] {3, 1, 2, 9, 4, 2},
            new[] {9, 2, -3, 1},
            new[] {7, 6, -5, -8, 9}
        };
        for (var i = 0; i < testArrs.Length; i++)
        {
            Console.WriteLine("Test Case #{0}:", i + 1);
        }
    }
}