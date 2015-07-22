import java.util.Arrays;

public class FindEquilibrium
{
    public static int findEquilibrium(int[] arr)
    {
        int leftSum = 0;
        int rightSum = 0;
        for (int i = 1; i < arr.length; i++)
            rightSum += arr[i];
        for (int i = 0; i < arr.length; i++)
        {
            // ASSERT:
            //      leftSum = arr[0] + ... + arr[i - 1]
            //     rightSum = arr[i + 1] + ... + arr[n - 1]
            if (leftSum == rightSum)
                return i;
            if (i < arr.length - 1)
            {
                leftSum += arr[i];
                rightSum -= arr[i + 1];
            }
        }
        return -1;
    }

    public static void main(String[] args)
    {
        int[][] test_arrs = {
                {},
                {-7, 1, 5, 2, -4, 3, 0},
                {1, 2, 3, 4, 5},
                {3, 1, 2, 9, 4, 2},
                {9, 2, -3, 1},
                {7, 6, -5, -8, 9}
        };
        for (int i = 0; i < test_arrs.length; i++)
        {
            System.out.printf("Test Case #%d: ", i + 1);
            System.out.println(Arrays.toString(test_arrs[i]));
            int index = findEquilibrium(test_arrs[i]);
            System.out.printf("    Equilibrium Index: %d\n", index);
        }
    }
}