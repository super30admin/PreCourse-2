//Time Complexity O(n log n)- when pivot divides array into two equal halves
//Space Complexity O(log n)

using System;

public class QuickSort
{
    // Partition method to place pivot element at its correct position
    private static int Partition(int[] arr, int low, int high)
    {
        int pivot = arr[high]; // Pivot element (choosing the last element as pivot)
        int i = low - 1; // Index of the smaller element

        for (int j = low; j < high; j++)
        {
            // If the current element is smaller than or equal to the pivot
            if (arr[j] <= pivot)
            {
                i++;
                // Swap arr[i] and arr[j]
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }

        // Swap arr[i + 1] and arr[high] (or pivot)
        int temp1 = arr[i + 1];
        arr[i + 1] = arr[high];
        arr[high] = temp1;

        return i + 1; // Return the partition index
    }

    // QuickSort method
    public static void QuickSortArray(int[] arr, int low, int high)
    {
        if (low < high)
        {
            // Find the partition index
            int pi = Partition(arr, low, high);

            // Recursively sort the elements before and after partition
            QuickSortArray(arr, low, pi - 1);  // Sort the left side
            QuickSortArray(arr, pi + 1, high); // Sort the right side
        }
    }

    // Method to print the array
    public static void PrintArray(int[] arr)
    {
        for (int i = 0; i < arr.Length; i++)
        {
            Console.Write(arr[i] + " ");
        }
        Console.WriteLine();
    }

    public static void Main(string[] args)
    {
        int[] arr = { 10, 7, 8, 9, 1, 5 };
        int n = arr.Length;

        Console.WriteLine("Unsorted array:");
        PrintArray(arr);

        QuickSortArray(arr, 0, n - 1);

        Console.WriteLine("Sorted array:");
        PrintArray(arr);
    }
}
