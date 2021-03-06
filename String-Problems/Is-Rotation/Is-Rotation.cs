using System;

public class IsRotationSolution
{
    public static bool IsRotation(string s, string t)
    {
        return s.Length == t.Length && (s + s).Contains(t);
    }

    /// <summary>
    /// The entry point.
    /// </summary>
    public static void Main()
    {
        var testStringPairs = new[]
        {
			new[] {"stackoverflow", "flowstackover"},
            new[] {"animal", "alanim"},
            new[] {"stackoverflow", "flowstackovez"},
            new[] {"stackoverflow", "flowstackove"}
		};
        var testCase = 1;
        foreach (var stringPair in testStringPairs)
        {
            var s = stringPair[0];
            var t = stringPair[1];
            Console.WriteLine("Test String Pair #{0}:", testCase);
            Console.WriteLine("({0}, {1}) {2} rotations of each other.",
                              s, t, IsRotation(s, t) ? "are" : "are not");
            testCase++;
        }
    }
}