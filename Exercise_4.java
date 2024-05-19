// Time Complexity : O(nlogN)
// Space Complexity : O(N)  for creating sub arrays
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : No

class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
        int n1 = m - l + 1; // elements in first subarray
        int n2 = r - m;     // elements in second subarray

        int L[] = new int[n1]; // temp array for left sub-array
        int R[] = new int[n2]; // temp array for right sub-array

        for (int i = 0; i < n1; ++i) {
            L[i] = arr[l + i]; // making the left sub array
        }
        for (int j = 0; j < n2; ++j) {
            R[j] = arr[m + 1 + j]; // making the right sub array
        }

        int i = 0, j = 0;
        int k = l;
        while (i < n1 && j < n2) { // filling up the new array
            if (L[i] <= R[j]) {
                arr[k++] = L[i++];
            } else {
                arr[k++] = R[j++];
            }
        }

        while (i < n1) { // filling up the new array with remaining elements
            arr[k++] = L[i++];
        }

        while (j < n2) {
            arr[k++] = R[j++];
        }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
        if (l < r) { // Check to see if low is less than high
            int mid = l + (r - l) / 2;
            sort(arr, l, mid); // recursively call sort
            sort(arr, mid + 1, r); // recursively call sort
            merge(arr, l, mid, r); // conquer - merge
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