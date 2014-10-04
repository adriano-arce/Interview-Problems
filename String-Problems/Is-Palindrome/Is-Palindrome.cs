using System;
using System.Linq;

public class IsPalindromeSolution
{
    /// <summary>
    /// Returns true iff s is a palindrome.
    /// Clarification to ask the interviewer:
    /// - Are whitespace, punctuation, and case considered important?
    /// - For this function, we assume that they are NOT important.
    /// </summary>
    /// <param name="s">The candidate palindrome string.</param>
    /// <returns>True iff s is a palindrome.</returns>
    public static bool IsPalindrome(string s)
    {
        // Strip out all whitespace and punctuation, and ignore case.
        var strippedChars = s.ToCharArray()
                             .Where(c => !char.IsWhiteSpace(c)
                                         && !char.IsPunctuation(c))
                             .ToArray();
        var stripped = new string(strippedChars).ToLower();

        // Compare the first half of the string with the second half.
        var len = stripped.Length;
        for (var i = 0; i < len; i++)
        {
            if (stripped[i] != stripped[len - 1 - i])
            {
                return false;
            }
        }
        return true;
    }
    
    /// <summary>
    /// Returns the raw representation of s. Surrounds s with single quotes
    /// and allows us to see newlines and tabs.
    /// </summary>
    /// <param name="s">The string to be processed.</param>
    /// <returns>The raw representation of s.</returns>
    public static string ToRepr(string s)
    {
        return "'" + s.Replace("\n", @"\n").Replace("\t", @"\t") + "'";
    }

    public static void Main()
    {
        var testStrings = new[] {
			"",
			"#$%^%$#",
			"rAcecar",
			"racecar",
			"ricecar",
			"abba",
			"12344329",
			"a@@#  b C \n\t d Eedc b  A",
			"a@@#  b C \n\t d Eedc b  z",
			"A man, a plan, a canal, Panama!"
		};
        var testCase = 1;
        foreach (var s in testStrings)
        {
            Console.WriteLine("Test String #{0}:", testCase);
            Console.WriteLine("{0} {1} a palindrome.",
                              ToRepr(s), IsPalindrome(s) ? "is" : "is not");
            testCase++;
        }

        Console.Write("\nPress any key to continue...");
        Console.ReadKey();
    }
}