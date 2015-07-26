using System;
using System.Collections.Generic;
using System.Diagnostics;

public class FindTwoSumSolution
{
    public static bool FindTwoSum(int[] arr, int target, out int i, out int j)
    {
        var sumDict = new Dictionary<int, int>();
        for (j = 0; j < arr.Length; j++)
        {
            if (sumDict.ContainsKey(arr[j]))
            {
                i = sumDict[arr[j]];
                return true;
            }
            sumDict[target - arr[j]] = j;
        }
        i = -1;
        j = -1;
        return false;
    }

    /// <summary>
    /// The entry point.
    /// </summary>
    public static void Main()
    {
        var testArrs = new[] 
        {
            new[] {8, 5, 6, 7},
            new[] {3, 9, 6, 2, 1, 5},
            new[] {3, 4, 5, 6}
        };
        var testTargets = new[] {13, 10, 12};
        Debug.Assert(testArrs.Length == testTargets.Length);
        for (var k = 0; k < testArrs.Length; k++)
        {
            Console.WriteLine("Test Case #{0}:", k + 1);
            int i, j;
            if (FindTwoSum(testArrs[k], testTargets[k], out i, out j))
                Console.WriteLine("    ({0}, {1})", i, j);
            else
                Console.WriteLine("    No two such indices exist.");
        }
    }
}