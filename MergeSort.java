// Time Complexity : O(n log n)
// Space Complexity : O(n) - due to the temporary arrays used during merge
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : No major issues. Just needed to be cautious with array indices during the merge step.

/*
Your code here along with comments explaining your approach:

This is an implementation of Merge Sort using the Divide and Conquer strategy.

1. The `sort` function recursively splits the array into two halves until the base case is reached (single element).
2. The `merge` function then merges two sorted halves by:
    - Creating temporary arrays for the left and right halves.
    - Comparing elements from each half and copying the smaller one into the main array.
    - Copying any remaining elements from the temporary arrays into the main array.
3. This ensures that at every level of recursion, the merged array is sorted.

The process repeats up the recursion stack, ultimately sorting the entire array.
*/

class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
        int[] temp = new int[r - l + 1];
        int i = l, j = m + 1;
        int k = 0;

        while(i <= m && j <= r){
            if(arr[i] <= arr[j]){
                temp[k++] = arr[i++];
            } else {
                temp[k++] = arr[j++];
            }
        }

        while(i <= m){
            temp[k++] = arr[i++];
        }  

        while(j <= r){
            temp[k++] = arr[j++];
        }

        for(int idx = 0; idx < temp.length; idx++){
            arr[l + idx] = temp[idx];
        }
    }

  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	    //Write your code here
        //Call mergeSort from here 
        if (l < r) {
            int mid = l + (r - l) / 2;

            // Sort first and second halves
            sort(arr, l, mid);
            sort(arr, mid + 1, r);

            // Merge the sorted halves
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