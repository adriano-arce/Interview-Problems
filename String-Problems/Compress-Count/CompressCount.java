public class CompressCount
{
    public static String compressCount(String s)
    {
        if (s == null || s.isEmpty())
            return s;
        StringBuilder compressed = new StringBuilder();
        int i = 0;
        while (i < s.length())
        {
            int j = i + 1;
            while (j < s.length() && s.charAt(j) == s.charAt(i))
                j++;
            // ASSERT: s.substring(i, j) is a run.
            compressed.append(s.charAt(i));
            compressed.append(j - i);
            i = j;
        }
        String candidate = compressed.toString();
        if (candidate.length() >= s.length())
            return s;
        return candidate;
    }

    public static String decompressCount(String s)
    {
        if (s == null || s.length() < 2 || !Character.isDigit(s.charAt(1)))
            return s;
        StringBuilder decompressed = new StringBuilder();
        int i = 0;
        while (i < s.length())
        {
            int j = i + 1;
            while (j < s.length() && Character.isDigit(s.charAt(j)))
                j++;
            // ASSERT: s.substring(i + 1, j) can be converted to an integer.
            int count = Integer.parseInt(s.substring(i + 1, j));
            for (int k = 0; k < count; k++)
                decompressed.append(s.charAt(i));
            i = j;
        }
        return decompressed.toString();
    }

    public static void main(String[] args)
    {
        String[] testStrings = {
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
        for (int i = 0; i < testStrings.length; i++)
        {
            String original = testStrings[i];
            String compressed = compressCount(original);
            String decompressed = decompressCount(compressed);
            System.out.printf("Test Case #%d: %s -> %s -> %s\n",
                    i + 1, original, compressed, decompressed);
        }
    }
}