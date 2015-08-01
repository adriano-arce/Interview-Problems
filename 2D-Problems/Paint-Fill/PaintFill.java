import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class PaintFill
{
    public enum Colour
    {
        Black, Red, Blue, Green, White;
    }

    public static void paintFill(Colour[][] grid, int x, int y, Colour newCol)
    {
        paintFill(grid, x, y, grid[x][y], newCol);
    }

    public static void paintFill(Colour[][] grid, int x, int y, Colour
            oldCol, Colour newCol)
    {
        int m = grid.length;
        int n = grid[0].length;
        if (0 <= x && x < m && 0 <= y && y < n && grid[x][y] == oldCol &&
                grid[x][y] != newCol)
        {
            grid[x][y] = newCol;
            paintFill(grid, x - 1, y, oldCol, newCol);
            paintFill(grid, x + 1, y, oldCol, newCol);
            paintFill(grid, x, y - 1, oldCol, newCol);
            paintFill(grid, x, y + 1, oldCol, newCol);
        }
    }


    public static void main(String[] args)
    {
        Map<Character, Colour> colourMap = new HashMap<>();
        colourMap.put('k', Colour.Black);
        colourMap.put('r', Colour.Red);
        colourMap.put('b', Colour.Blue);
        colourMap.put('g', Colour.Green);
        colourMap.put('w', Colour.White);

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
                originalGrid[i][j] = colourMap.get(charGrid[i][j]);

        int[][] testPositions = {
                {0, 0},
                {0, 0},
                {1, 4},
                {1, 4},
                {1, 4},
                {2, 4},
                {2, 4},
                {2, 4}
        };
        Colour[] testColours = {
                Colour.Black,
                Colour.Blue,
                Colour.Black,
                Colour.Blue,
                Colour.Red,
                Colour.Black,
                Colour.Blue,
                Colour.Red
        };
        assert testPositions.length == testColours.length;
        for (int i = 0; i < testPositions.length; i++)
        {
            Colour[][] grid = Arrays.copyOf(originalGrid, originalGrid.length);
            int x = testPositions[i][0];
            int y = testPositions[i][1];
            Colour newCol = testColours[i];
            System.out.printf("Test Case #%d: (%d, %d, %s)\n", i + 1, x, y,
                    newCol.toString());

            paintFill(grid, x, y, newCol);
            System.out.println(Arrays.deepToString(grid));
        }
    }
}