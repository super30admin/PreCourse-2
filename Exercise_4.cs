// Time Complexity O(nlogn)
//Space Complexity O(n)

using System;

public class MergeSort
{
    public static void Merge(int[] arr, int left, int mid, int right)
    {
        // Sizes of two subarrays to be merged
        int n1 = mid - left + 1;
        int n2 = right - mid;

        // temp arrays
        int[] L = new int[n1];
        int[] R = new int[n2];

        // Copy data to temp arrays
        for (int i = 0; i < n1; i++)
            L[i] = arr[left + i];
        for (int j = 0; j < n2; j++)
            R[j] = arr[mid + 1 + j];

        // Merge the temp arrays
        int k = left; // Initial index of merged subarray
        int i1 = 0, j1 = 0; // Initial indexes of L[] and R[]

        while (i1 < n1 && j1 < n2)
        {
            if (L[i1] <= R[j1])
            {
                arr[k] = L[i1];
                i1++;
            }
            else
            {
                arr[k] = R[j1];
                j1++;
            }
            k++;
        }

        // Copy the remaining elements of L[] if any
        while (i1 < n1)
        {
            arr[k] = L[i1];
            i1++;
            k++;
        }

        // Copy the remaining elements of R[] if any
        while (j1 < n2)
        {
            arr[k] = R[j1];
            j1++;
            k++;
        }
    }

    public static void MergeSortArray(int[] arr, int left, int right)
    {
        if (left < right)
        {
            // Find the middle point
            int mid = left + (right - left) / 2;

            // Recursively sort the first and second halves
            MergeSortArray(arr, left, mid);
            MergeSortArray(arr, mid + 1, right);

            // Merge the sorted halves
            Merge(arr, left, mid, right);
        }
    }

    // Utility function to print the array
    public static void PrintArray(int[] arr)
    {
        for (int i = 0; i < arr.Length; i++)
        {
            Console.Write(arr[i] + " ");
        }
        Console.WriteLine();
    }

    // Main function to test the merge sort
    public static void Main(string[] args)
    {
        int[] arr = { 12, 11, 13, 5, 6, 7 };
        Console.WriteLine("Given array:");
        PrintArray(arr);

        MergeSortArray(arr, 0, arr.Length - 1);

        Console.WriteLine("\nSorted array:");
        PrintArray(arr);
    }
}
