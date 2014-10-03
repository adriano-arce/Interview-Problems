using System;
using System.Linq;

public class IsPalindromeSolution
{
    // Returns true iff s is a palindrome.
    // Clarification to ask the interviewer:
    // - Are whitespace, punctuation, and case considered important?
    // - For this function, we assume that they are NOT important.
    public static bool IsPalindrome(string s)
    {
        // Strip out all whitespace and punctuation, and ignore case.
        var strippedChars = s.ToCharArray()
                             .Where(c => !char.IsWhiteSpace(c) && !char.IsPunctuation(c))
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
            Console.WriteLine(IsPalindrome(s) ? "Palindrome." : "Not a palindrome.");
            testCase++;
        }

        Console.WriteLine();
        Console.WriteLine("Press any key to continue...");
        Console.ReadKey();
    }
}