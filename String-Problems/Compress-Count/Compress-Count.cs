using System;
using System.Text;

public class CompressCountSolution
{
    /// <summary>
    /// Compresses the given string by replacing each run of some character c
    /// of length k > 0 with ck instead, assuming that such a compression
    /// would decrease the length of the string.
    /// </summary>
    /// <param name="s">The string to be compressed.</param>
    /// <returns>The compressed string (or s).</returns>
    public static string CompressCount(string s)
    {
        if (string.IsNullOrEmpty(s))
        {
            return s;
        }
        var compressed = new StringBuilder();
        var i = 0;
        while (i < s.Length)
        {
            var j = i + 1;
            while (j < s.Length && s[j] == s[i])
            {
                j++;
            }
            // ASSERT: s.Substring(i, j - i) is a run.
            compressed.Append(s[i]);
            compressed.Append(j - i);
            i = j;
        }
        var candidate = compressed.ToString();
        if (candidate.Length < s.Length)
            return candidate;
        return s;
    }

    /// <summary>
    /// Decompresses the given compressed string into its original form, if
    /// necessary.
    /// </summary>
    /// <param name="s">The compressed string to be decompressed.</param>
    /// <returns>The decompressed string (or s).</returns>
    public static string DecompressCount(string s)
    {
        if (s == null || s.Length < 2 || !Char.IsDigit(s, 1))
        {
            return s;
        }
        var decompressed = new StringBuilder();
        var i = 0;
        while (i < s.Length)
        {
            var j = i + 1;
            while (j < s.Length && Char.IsDigit(s, j))
            {
                j++;
            }
            // ASSERT: s.substring(i+1, j-i-1) can be converted to an int.
            var count = int.Parse(s.Substring(i + 1, j - i - 1));
            for (var k = 0; k < count; k++)
            {
                decompressed.Append(s[i]);
            }
            i = j;
        }
        return decompressed.ToString();
    }

    /// <summary>
    /// The entry point.
    /// </summary>
    public static void Main()
    {
        var testStrings = new[]
        {
            "aabcccccaaa",
            "",
            "p",
            "pq",
            null,
            "abcde",
            "bbbc",
            "bbbcc",
            "aaaaaaaaaaaaabbbbccc"
		};
        for (var i = 0; i < testStrings.Length; i++)
        {
            var original = testStrings[i];
            var compressed = CompressCount(original);
            var decompressed = DecompressCount(compressed);
            Console.WriteLine("Test Case #{0}: {1} -> {2} -> {3}",
                i + 1, original, compressed, decompressed);
        }
    }
}