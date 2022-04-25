using System;
namespace Algorithms
{
    /// Time Complexity : O(nLog n), worst case O(n2)
    // Space Complexity :O(n)
    // Did this code successfully run on Leetcode : Tested on VS
    // Any problem you faced while coding this : Referred online
    public class QuickSort
    {
        /* This function takes last element as pivot, 
           places the pivot element at its correct 
           position in sorted array, and places all 
           smaller (smaller than pivot) to left of 
           pivot and all greater elements to right 
           of pivot */
        void swap(int[] arr, int i, int j)
        {
            //Your code here
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;

        }

        int partition(int[] arr, int low, int high)
        {
            //Write code here for Partition and Swap
            int pivot = arr[high];
            int partitionIndex = low;
            for(int i=low;i < high; i++)
            {
                if (arr[i] < pivot)
                {
                    swap(arr, i, partitionIndex);
                    partitionIndex++;
                }
            }
            swap(arr, partitionIndex, high);
            return partitionIndex;
        }
        /* The main function that implements QuickSort() 
          arr[] --> Array to be sorted, 
          low  --> Starting index, 
          high  --> Ending index */
        public void sort(int[] arr, int low, int high)
        {
            // Recursively sort elements before
            // partition and after partition 
            if (low < high)
            {
                int partitionIndex = partition(arr, low, high);
                sort(arr, low, partitionIndex - 1);
                sort(arr, partitionIndex + 1, high);
            }
            
        }

        /* A utility function to print array of size n */
        public void printArray(int[] arr)
        {
            int n = arr.Length;
            for (int i = 0; i < n; ++i)
                Console.WriteLine(arr[i] + " ");

        }

    }

}
