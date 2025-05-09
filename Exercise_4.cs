
using System;
/*
Space complexity - O(n)
Time complexity - O(nlog n)

OUTPUT -
Given Array
12 
11 
13 
5 
6 
7 


Sorted array
5 
6 
7 
11 
12 
13

Approach - The array is divided into halves recursively and then merged baxck together as per their value while merging resulting in a sorted array.

*/

namespace Precourse2
{
    public class MergeSort
    {
        // Merges two subarrays of arr[]. 
        // First subarray is arr[l..m] 
        // Second subarray is arr[m+1..r] 
        void merge(int[] arr, int l, int m, int r)
        {
            //Your code here
            int[] temp = new int[r - l + 1];
            int i = l, j = m + 1, k = 0;

            while (i <= m && j <= r)
            {
                if (arr[i] <= arr[j])
                {
                    temp[k++] = arr[i++];
                }
                else
                {
                    temp[k++] = arr[j++];
                }
            }

            while (i <= m)
            {
                temp[k++] = arr[i++];
            }

            while (j <= r)
            {
                temp[k++] = arr[j++];
            }

            for (int a = 0; a < temp.Length; a++)
            {
                arr[l + a] = temp[a];
            }
        }

        // Main function that sorts arr[l..r] using 
        // merge() 
        void sort(int[] arr, int l, int r)
        {
            //Write your code here
            //Call mergeSort from here
            if (l>=r)
                return;

            int m = l+(r-l)/2;

            sort(arr, l, m);
            sort(arr, m+1, r);

            merge(arr, l, m, r);
        }

        /* A utility function to print array of size n */
        public static void printArray(int[] arr)
        {
            int n = arr.Length;
            for (int i = 0; i < n; ++i)
                Console.WriteLine(arr[i] + " ");
            Console.WriteLine();
        }

        // Driver method 
        public static void Main(String[] args)
        {
            int[] arr = { 12, 11, 13, 5, 6, 7 };

            Console.WriteLine("Given Array");
            printArray(arr);

            MergeSort ob = new MergeSort();
            ob.sort(arr, 0, arr.Length - 1);

            Console.WriteLine("\nSorted array");
            printArray(arr);
        }
    }
}
