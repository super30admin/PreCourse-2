// Time Complexity : O(nlogn)
// Space Complexity : O(n)

import java.util.Arrays;

class MergeSort 
{ 
    private int[] tempArr;
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
        //Your code here  
        int i = l;
        int j = m + 1;
        int k = l;

        // Merge the temporary arrays
        while(i <= m && j <= r) {
            if (arr[i] <= arr[j]) {
                tempArr[k++] = arr[i++];
            } 
            else {
                tempArr[k++] = arr[j++];
            }
        }

        // Copy any remaining elements from left subarray 
        while (i <= m) {
            tempArr[k++] = arr[i++];
        }

        // Copy any remaining elements from right subarray
        while (j <= r) {
            tempArr[k++] = arr[j++];
        }

        for (int p = l; p <= r; p++) {
            arr[p] = tempArr[p];
        }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	    //Write your code here
        //Call mergeSort from here 
        if(l < r) {
            int mid = l + (r - l) / 2;
            sort(arr, l, mid);
            sort(arr, mid + 1, r);
            merge(arr, l, mid , r);
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
        ob.tempArr = new int[arr.length];
        ob.sort(arr, 0, arr.length-1); 
  
        System.out.println("\nSorted array"); 
        printArray(arr); 
    } 
} 