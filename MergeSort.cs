using System;
namespace Algorithms
{
    /// Time Complexity : O(nLog n)
    // Space Complexity :O(n)
    // Did this code successfully run on Leetcode : Tested on VS
    // Any problem you faced while coding this : Referred online
    public class MergeSort
    {

        // Merges two subarrays of arr[]. 
        // First subarray is arr[l..m] 
        // Second subarray is arr[m+1..r] 
        public void merge(int[] arr, int l, int m, int r)
        {
            //size of sub arrays

            int n1 = m - l + 1;
            int n2 = r - m;

            //initialize left and right array

            int[] L = new int[n1];
            int[] R = new int[n2];

            int i, j;

            //fill L and R

            for (i = 0; i < n1; ++i)
            {
                L[i] = arr[l + i];
            }
            for (j = 0; j < n2; ++j)
            {
                R[j] = arr[m + 1 + j];
            }

            i = 0;j = 0; int k = l;

            while(i<n1 && j < n2)
            {
                if(L[i] < R[j])
                {
                    arr[k] = L[i];
                    i++;
                    k++;
                }
                else
                {
                    arr[k] = R[j];
                    j++;
                    k++;
                }
            }
            while (i < n1)
            {
                arr[k] = L[i];
                i++;
                k++;
            }
            while(j < n2)
            {
                arr[k] = R[j];
                j++;
                k++;
            }
        }

        // Main function that sorts arr[l..r] using 
        // merge() 
        public void sort(int[] arr, int l, int r)
        {
            //Write your code here
            if (l < r)
            {
                //find mid point
                int mid = l + (r - l) / 2;
                sort(arr, l, mid);
                sort(arr, mid + 1, r);

                //Call mergeSort from here 
                merge(arr, l, mid, r);
            }
            
        }

        /* A utility function to print array of size n */
        public void printArray(int[] arr)
        {
            int n = arr.Length;
            for (int i = 0; i < n; ++i)
                Console.WriteLine(arr[i] + " ");
            // System.out.println();
        }

        
    }
}


