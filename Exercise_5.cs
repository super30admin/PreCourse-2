// Time Complexity: O(nlogn)
// Space Complexity: O(logn)
using System;

public class IterativeQuickSort
{
    public static void Swap(ref int a, ref int b)
    {
        int temp = a;
        a = b;
        b = temp;
    }

    // Partition function similar to the one used in recursive quicksort
    public static int Partition(int[] arr, int low, int high)
    {
        int pivot = arr[high]; // Pivot is the last element
        int i = low - 1; // Index of smaller element

        for (int j = low; j < high; j++)
        {
            // If the current element is smaller than or equal to the pivot
            if (arr[j] <= pivot)
            {
                i++;
                // Swap arr[i] and arr[j]
                Swap(ref arr[i], ref arr[j]);
            }
        }
        // Swap arr[i+1] and arr[high] (or pivot)
        Swap(ref arr[i + 1], ref arr[high]);
        return i + 1;
    }

    public static void QuickSortIterative(int[] arr, int low, int high)
    {
        // Create an auxiliary stack
        int[] stack = new int[high - low + 1];

        // Initialize top of stack
        int top = -1;

        // Push initial values of low and high to the stack
        stack[++top] = low;
        stack[++top] = high;

        // Keep popping from stack while it's not empty
        while (top >= 0)
        {
            // Pop high and low
            high = stack[top--];
            low = stack[top--];

            // Partition the array and get the pivot index
            int pivotIndex = Partition(arr, low, high);

            // If there are elements on the left side of the pivot, push them to the stack
            if (pivotIndex - 1 > low)
            {
                stack[++top] = low;
                stack[++top] = pivotIndex - 1;
            }

            // If there are elements on the right side of the pivot, push them to the stack
            if (pivotIndex + 1 < high)
            {
                stack[++top] = pivotIndex + 1;
                stack[++top] = high;
            }
        }
    }

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
        int[] arr = { 4, 3, 5, 2, 1, 3, 2, 3 };
        Console.WriteLine("Given array:");
        PrintArray(arr);

        QuickSortIterative(arr, 0, arr.Length - 1);

        Console.WriteLine("Sorted array:");
        PrintArray(arr);
    }
}
