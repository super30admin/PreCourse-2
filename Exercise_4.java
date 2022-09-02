// Time Complexity : O(nLogN)
// Space Complexity : O(n)
// Did this code successfully run on Leetcode :
// Any problem you faced while coding this : teh rays.copyOfRange method, i had used
// incorrect ranges like Arrays.copyOfRange(arr, l, m) and Arrays.copyOfRange(arr, m + 1, r)
// also i was initializing k = 0 in every iteration.
// All in all, i was trying to merge two sorted arrays
import java.util.Arrays;

class MergeSort
{
    // Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]
    void merge(int arr[], int l, int m, int r)
    {
       //Your code here
        int[] a1 = Arrays.copyOfRange(arr, l, m + 1);
        int[] a2 = Arrays.copyOfRange(arr, m + 1 , r + 1);

        int i=0, j=0, k=l;

        while(i< a1.length && j < a2.length) {
            if(a1[i] <= a2[j]) {
                arr[k] = a1[i];
                i++;
            } else {
                arr[k] = a2[j];
                j++;
            }
            k++;
        }

        for(; i < a1.length; i++) {
            arr[k] = a1[i];
            k++;
        }

        for (; j < a2.length; j++) {
            arr[k] = a2[j];
            k++;
        }

    }

    // Main function that sorts arr[l..r] using
    // merge()
    void sort(int arr[], int l, int r)
    {
	//Write your code here
        int mid = (l + r) / 2;
        //Call mergeSort from here
        if (l < r) {
            sort(arr, l, mid);
            sort(arr, mid+1, r);
            merge(arr, l, mid, r);
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