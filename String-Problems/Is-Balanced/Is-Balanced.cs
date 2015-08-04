using System;
using System.Collections.Generic;
using System.Linq;

public class IsBalancedSolution
{
    public static bool IsBalanced(string s)
    {
        var bracketDict = new Dictionary<char, char>()
        {
            {'{', '}'},
            {'(', ')'},
            {'[', ']'}
        };
        var rightBrackets = new HashSet<char>(bracketDict.Values);
        var bracketStack = new Stack<char>();
        foreach (var c in s)
        {
            if (bracketDict.ContainsKey(c))
                bracketStack.Push(bracketDict[c]);
            else if (rightBrackets.Contains(c))
            {
                if (bracketStack.Count == 0 || bracketStack.Peek() != c)
                    return false;
                bracketStack.Pop();
            }
        }
        return bracketStack.Count == 0;
    }

    /// <summary>
    /// The entry point.
    /// </summary>
    public static void Main()
    {
        var testStrings = new[]
        {
            "(2 + y) - e^{2x + 3} * [7x] / [sin(2e^{7x})]",
            "5(2 + x]",
            "4)x + 3(",
            "[][](){{}}[()]",
            "[[[(({})[])]]{()}]",
            "((("
		};
        for (var i = 0; i < testStrings.Length; i++)
        {
            Console.WriteLine("Test String #{0}: {1}", i + 1, testStrings[i]);
            Console.WriteLine("    " + IsBalanced(testStrings[i]));
        }
    }
}