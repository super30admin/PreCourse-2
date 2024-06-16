/*
    1. Time Complexity : O(nlogn)   
    2. Space Complexity : O(n)
    3. Did this code successfully run on Leetcode : Yes, Solved Problem - 912. Sort an Array 
    4. Any problem you faced while coding this : -
 */

class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) {
        int n1 = m - l + 1, n2 = r - m, i = 0, j = 0, k = l;
        int left[] = new int[n1];
        for (i = 0; i < n1; ++i)
            left[i] = arr[l + i];
        int right[] = new int[n2];
        for (i = 0; i < n2; ++i)
            right[i] = arr[m + 1 + i];
        i = 0;
        while (i < n1 && j < n2) {
            if (left[i] < right[j]) {
                arr[k++] = left[i++];
            } else {
                arr[k++] = right[j++];
            }
        }
        while (i < n1) {
            arr[k++] = left[i++]; 
        }
        while (j < n2) {
            arr[k++] = right[j++];
        }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) {
        if (l < r) {
            int mid = l + (r - l) / 2;
            sort(arr, l, mid);
            sort(arr, mid + 1, r);
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