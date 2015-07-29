using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;

public class PaintFillSolution
{
    public enum Colour 
    {
        Black = 'k',
        Red = 'r',
        Blue = 'b',
        Green = 'g',
        White = 'w'
    }

    public static void PaintFill(Colour[][] grid, int x, int y, Colour newCol)
    {
        PaintFill(grid, x, y, grid[x][y], newCol);
    }

    /// <summary>
    /// Paint fills (x, y) and all surrounding neighbours coloured with oldCol
    /// with newCol. Uses recursive DFS.
    /// </summary>
    /// <param name="grid">The rectangular grid of colours.</param>
    /// <param name="x">The row of the position to be coloured.</param>
    /// <param name="y">The column of the position to be coloured.</param>
    /// <param name="oldCol">The old colour.</param>
    /// <param name="newCol">The new colour.</param>
    public static void PaintFill(Colour[][] grid, int x, int y, Colour oldCol,
        Colour newCol)
    {
        var m = grid.Length;
        var n = grid[0].Length;
        if (0 <= x && x < m && 0 <= y && y < n
            && grid[x][y] == oldCol && grid[x][y] != newCol)
        {
            grid[x][y] = newCol;
            PaintFill(grid, x - 1, y, oldCol, newCol);
            PaintFill(grid, x + 1, y, oldCol, newCol);
            PaintFill(grid, x, y - 1, oldCol, newCol);
            PaintFill(grid, x, y + 1, oldCol, newCol);
        }
    }

    /// <summary>
    /// The entry point.
    /// </summary>
    public static void Main()
    {
        var originalGrid = new[]
        {
            "kkkkkkkkwwwkkkkkkkkrrkk".ToCharArray().Select(c => (Colour)c),
            "kkkkbbbbbbbbbbbbbbkkkkk".ToCharArray().Select(c => (Colour)c),
            "kkkrrrbbbbbbbbbbbbbbbbb".ToCharArray().Select(c => (Colour)c),
            "kkkkbkkkkkkkkkkrrrkkbkk".ToCharArray().Select(c => (Colour)c),
            "kgkkbkkkkkkkkkkkkkkkbkk".ToCharArray().Select(c => (Colour)c),
            "kkkkbkkkkkkkkkkkkkkkbkk".ToCharArray().Select(c => (Colour)c),
            "kkkbbbbkkkkkkkkkkkkbbbb".ToCharArray().Select(c => (Colour)c)
        };
        var testPositions = new[]
        {
            new[] {0, 0},
            new[] {0, 0},
            new[] {1, 4},
            new[] {1, 4},
            new[] {1, 4},
            new[] {2, 4},
            new[] {2, 4},
            new[] {2, 4}
        };
        var testColours = new[]
        {
            Colour.Black,
            Colour.Blue,
            Colour.Black,
            Colour.Blue,
            Colour.Red,
            Colour.Black,
            Colour.Blue,
            Colour.Red
        };
        Debug.Assert(testPositions.Length == testColours.Length);
        for (var i = 0; i < testPositions.Length; i++)
        {
            // Clone the original grid and extract input for current test case.
            var grid = originalGrid.Select(c => c.ToArray()).ToArray();
            var x = testPositions[i][0];
            var y = testPositions[i][1];
            var newCol = testColours[i];
            Console.WriteLine("Test Case #{0}: ({1}, {2}, {3})",
                i + 1, x, y, newCol);

            PaintFill(grid, x, y, newCol);
            Console.WriteLine(string.Join("\n", grid.Select(row =>
                string.Join("", row.Select(c => (char)c)))));
        }
    }
}