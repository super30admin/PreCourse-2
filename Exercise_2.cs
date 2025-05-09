
using System;
/*
Space complexity - O(n)
Time complexity - O(nlog n)

OUTPUT -
sorted array
1 
5 
7 
8 
9 
10 

Approach - Recursively traverse the array by splitting the array elements which  are less than pivot to the left of pivot and the values greater to the right.

*/

namespace Precourse2
{
    class QuickSort
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
            int temp = low;

            for(int i=low; i<high;i++)
            {
                if(arr[i]<pivot)
                {
                    swap(arr, temp, i);
                    temp++;
                }
            }

            swap(arr, temp, high);
            return temp;
        }
        /* The main function that implements QuickSort() 
          arr[] --> Array to be sorted, 
          low  --> Starting index, 
          high  --> Ending index */
        void sort(int[] arr, int low, int high)
        {
            // Recursively sort elements before 
            // partition and after partition

            if(low<high)
            {
                int p = partition(arr, low, high);

                sort(arr, low, p - 1);
                sort(arr, p + 1, high);
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

        // Driver program 
        public static void Main(String[] args)
        {
            int[] arr = { 10, 7, 8, 9, 1, 5 };
            int n = arr.Length;

            QuickSort ob = new QuickSort();
            ob.sort(arr, 0, n - 1);

            Console.WriteLine("sorted array");
            printArray(arr);
        }
    }
}