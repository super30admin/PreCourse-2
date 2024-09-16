//Time Complexity O(1) for sorted array
//Space Complexity O(1)

using System;

public class BinarySearch
{
    public static int Search(int[] arr, int target)
    {
        int left = 0;
        int right = arr.Length - 1;

        while (left <= right)
        {
            int mid = left + (right - left) / 2;

            // Check if target is present at mid
            if (arr[mid] == target)
            {
                return mid; // Target found at index mid
            }

            // If target is greater, ignore left half
            if (arr[mid] < target)
            {
                left = mid + 1;
            }
            // If target is smaller, ignore right half
            else
            {
                right = mid - 1;
            }
        }

        // Target not found in the array
        return -1;
    }

    public static void Main(string[] args)
    {
        // Sorted array
        int[] arr = { 2, 3, 4, 10, 40 };
        int target = 10;

        int result = Search(arr, target);

        if (result != -1)
        {
            Console.WriteLine($"Element found at index {result}");
        }
        else
        {
            Console.WriteLine("Element not found");
        }
    }
}
