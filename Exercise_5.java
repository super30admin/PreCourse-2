// Time Complexity : O(nlogn)
// Space Complexity : O(n)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : No

class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       int[] mergedArray = new int[r-l];

       int i = l, j = m, k = 0;

       while(i < m && j < r) {

            if(arr[i] < arr[j]) {               // if the left array has the smallest value then copy the left one
                mergedArray[k++] = arr[i++];
            } else {                            // if the right array has the smallest value then copy the right one
                mergedArray[k++] = arr[j++];
            }
       }

       // Copy all the remaining elements from left or right arrays
       while(i < m) {
           mergedArray[k++] = arr[i++];
       }

       while(j < r) {
            mergedArray[k++] = arr[j++];
       }

       // Copy the result into the original array
        for(int itr = 0; itr < mergedArray.length; itr++) {
            arr[l + itr] = mergedArray[itr];
        }
       
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
    
        if(r - l == 1) {
            return;
        }

        // Dividing array into half recursively until there's only one element
        int m = l + (r - l) / 2;
        sort(arr, l, m);
        sort(arr, m, r);

        // Merging two unsorted arrays
        merge(arr, l, m, r+1);
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