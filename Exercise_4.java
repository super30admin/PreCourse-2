// Time Complexity : O (n logn) - dividing takes log n and merging takes n
// Space Complexity : O(n) - temp array storage
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : Had to refresh the sorting algorithms


// Your code here along with comments explaining your approach
// Dividing the array in middle and sorting left + right and then merging it back in
class MergeSort {
    // Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]
    void merge(int arr[], int l, int m, int r) {
        // temp arrays
        int t1 = m - l + 1;
        int t2 = r - m;
        int[] L = new int[t1];
        int[] R = new int[t2];

        for (int i = 0; i < t1; i++)
            L[i] = arr[l + i];
        for (int j = 0; j < t2; j++)
            R[j] = arr[m + 1 + j];

        int i = 0, j = 0;
        int k = l;
        while (i < t1 && j < t2) {
            if (L[i] <= R[j]) {
                arr[k] = L[i];
                i++;
            } else {
                arr[k] = R[j];
                j++;
            }
            k++;
        }

        // remaining elements from t1
        while (i < t1) {
            arr[k] = L[i];
            i++;
            k++;
        }

        // remaining elements from t1
        while (j < t2) {
            arr[k] = R[j];
            j++;
            k++;
        }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here 
        if (l < r) {
            int mid = l + (r-l)/2;
            sort(arr, l, mid);
            sort(arr, mid +1, r);

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