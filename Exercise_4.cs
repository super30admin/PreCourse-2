// Time Complexity :O(NlogN) where N = number of elements in array
// Space Complexity : O(N) - extra space to store the temp left and right array 
using System;

class MergeSort
{
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int[] arr, int l, int m, int r)
    {
        //Your code here
        int l1 = (m - l + 1);
        int l2 = (r - m);
        int[] leftArray = new int[l1];
        int[] rightArray = new int[l2];

        for (int i = 0; i < l1; i++)
        {
            leftArray[i] = arr[l + i];
        }
        for (int i = 0; i < l2; i++)
        {
            rightArray[i] = arr[m+1+i];
        }

        int leftIndex = 0;
        int rightIndex = 0;
        int k = l;

        while (leftIndex < l1 && rightIndex < l2)
        {
            if (leftArray[leftIndex] <= rightArray[rightIndex])
            {
                arr[k] = leftArray[leftIndex];
                k++;
                leftIndex++;
            }
            else
            {
                arr[k] = rightArray[rightIndex];
                k++;
                rightIndex++;
            }  
        }
        while (leftIndex < l1)
        {
            arr[k] = leftArray[leftIndex];
            k++;
            leftIndex++;
        }
        while (rightIndex < l2)
        {
            arr[k] = rightArray[rightIndex];
            k++;
            rightIndex++;
        }
    }

    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int[] arr, int l, int r)
    {
        //Write your code here
        //Call mergeSort from here 
        if (l < r)
        {
            int mid = (l + r) / 2;
            sort(arr, l, mid);
            sort(arr, mid + 1, r);
            merge(arr, l, mid, r);
        }
    }

    /* A utility function to print array of size n */
    static void printArray(int[] arr)
    {
        int n = arr.Length;
        for (int i = 0; i < n; ++i)
            Console.WriteLine(arr[i] + " ");
        Console.WriteLine();
    }

    // Driver method 
    public static void Main(string[] args)
    {
        int[] arr = { 12, 11, 13, 5, 6, 7 };

        Console.WriteLine("Given Array");
        printArray(arr);

        MergeSort ob = new MergeSort();
        ob.sort(arr, 0, arr.Length - 1);

        Console.WriteLine("\nSorted array");
        printArray(arr);
        Console.ReadLine();
    }
}