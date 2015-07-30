public class PaintFill
{
    public enum Colour
    {
        Black('k'), Red('r'), Blue('b'), Green('g'), White('w');

        Colour(final char asChar)
        {
            this.asChar = asChar;
        }

        private final char asChar;

        public char asChar()
        {
            return asChar;
        }
    }

    public static void main(String[] args)
    {
        char[][] charGrid = {
                "kkkkkkkkwwwkkkkkkkkrrkk".toCharArray(),
                "kkkkbbbbbbbbbbbbbbkkkkk".toCharArray(),
                "kkkrrrbbbbbbbbbbbbbbbbb".toCharArray(),
                "kkkkbkkkkkkkkkkrrrkkbkk".toCharArray(),
                "kgkkbkkkkkkkkkkkkkkkbkk".toCharArray(),
                "kkkkbkkkkkkkkkkkkkkkbkk".toCharArray(),
                "kkkbbbbkkkkkkkkkkkkbbbb".toCharArray()
        };
        int m = charGrid.length;
        int n = charGrid[0].length;
        Colour[][] originalGrid = new Colour[m][n];
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                originalGrid[i][j] = Colour.valueOf(String
                        .valueOf(charGrid[i][j]));
    }
}