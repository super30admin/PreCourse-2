//Time Complexity: O(NlogN) -> LogN comes from dividing the array into half and N from comparing at each level
// Space Complexity: O(N) -> Due to storing the temp left and right arrays.

import java.awt.image.renderable.RenderableImage;
import java.lang.reflect.Array;
import java.util.Arrays;

class MergeSort
{
    // Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]
    void merge(int arr[], int l, int m, int r)
    {
       int[] leftArray = new int[m-l+1];
       int[] rightArray = new int[r-m];
       leftArray = Arrays.copyOfRange(arr, l, m+1);
       rightArray = Arrays.copyOfRange(arr, m+1, r+1);

       int index = l;
       int i = 0, j = 0 ;
       while (i < m-l+1 && j < r-m) {
           if (leftArray[i] <= rightArray[j]) {
               arr[index] = leftArray[i];
               i++;
           } else {
               arr[index] = rightArray[j];
               j++;
           }
           index++;
       }

       while (i < m-l+1) arr[index++] = leftArray[i++];
       while (j < r-m) arr[index++] = rightArray[j++];
    }

    // Main function that sorts arr[l..r] using
    // merge()
    void sort(int arr[], int l, int r)
    {
        int middle = l + (r - l)/2;
	    if (l < r) {
            sort(arr, l, middle);
            sort(arr, middle + 1, r);
            merge(arr, l, middle, r);
        }
    }

    /* A utility function to print array of size n */
    static void printArray(int arr[])
    {
        int n = arr.length;
        for (int i=0; i<n; ++i)
            System.out.print(arr[i] + " ");
        System.out.println();
    }

    // Driver method
    public static void main(String args[])
    {
        int arr[] = {12, 11, 13, 5, 6, 7};

        System.out.println("Given Array");
        printArray(arr);

        MergeSort ob = new MergeSort();
        ob.sort(arr, 0, arr.length-1);

        System.out.println("\nSorted array");
        printArray(arr);
    }
}