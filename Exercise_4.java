// Time Complexity : O(N Log N)
// Space Complexity: O(N Log N)
// Did this code successfully run on Leetcode : N/A
// Any problem you faced while coding this : No


// Your code here along with comments explaining your approach

class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       // Find lengths of two subarrays to be merged 
       int length1 = m - l + 1;
       int length2 = r - m;
       
       // Create temp arrays
       int[] left = new int[length1];
       int[] right = new int[length2];
       
       // Copy the sorted left & right halfs to temp arrays
       for(int i=0; i < length1; i++) {
            left[i] = arr[l + i];
       }

       for(int j=0; j < length2; j++) {
            right[j] = arr[m + 1 + j];
       }

       // Initial indexes of left and right sub arrays
       int i = 0;
       int j = 0;
       int k = l;

       // Merge sorted halfs into original array
       while(i < left.length && j < right.length) {
            if(left[i] <= right[j]) {
                arr[k] = left[i];
                i++;
                k++;
            } else {
                arr[k] = right[j];
                j++;
                k++;
            }
       }
       // If the right array is smaller than left array
       // Then copy all the remaining items from left array and place it in original array
       while(i < left.length) {
            arr[k] = left[i];
            i++;
            k++;
       }
        // If the left array is smaller than right array
       // Then copy all the remaining items from right array and place it in original array
       while(j < right.length) {
            arr[k] = right[j];
            j++;
            k++;
       }

    }

    void sort(int arr[], int l, int r) 
    { 
        if(l < r) {
            // Find the middle point of arr
            int mid = (l + r) / 2;

            sort(arr, l, mid);  // Sort left half
            sort(arr, mid + 1, r); // Sort right half
            merge(arr, l, mid, r); // Merge sorted halfs
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