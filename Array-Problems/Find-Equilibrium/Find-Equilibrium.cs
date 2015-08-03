using System;

public class FindEquilibriumSolution
{
    public static int FindEquilibrium(int[] arr)
    {
        int leftSum = 0;
        int rightSum = 0;
        for (int i = 1; i < arr.Length; i++)
            rightSum += arr[i];
        for (int i = 0; i < arr.Length; i++)
        {
            if (leftSum == rightSum)
                return i;
            if (i + 1 < arr.Length)
            {
                leftSum += arr[i];
                rightSum -= arr[i + 1];
            }
        }
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
            new[] {-7, 1, 5, 2, -4, 3, 0},
            new[] {1, 2, 3, 4, 5},
            new[] {3, 1, 2, 9, 4, 2},
            new[] {9, 2, -3, 1},
            new[] {7, 6, -5, -8, 9}
        };
        for (var i = 0; i < testArrs.Length; i++)
        {
            Console.WriteLine("Test Case #{0}: [{1}]", i + 1, string.Join(", ", testArrs[i]));
            Console.WriteLine("    Equilibrium Index: {0}", FindEquilibrium(testArrs[i]));
        }
    }
}