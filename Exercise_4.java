// Time Complexity : O(nlogn) where n is the number of elements in the array
// Space Complexity : O(n) where n is the number of elements in the array
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : No

class Exercise_4 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {
        //Your code here
        // Find sizes of two subarrays to be merged
        int leftLength = m - l + 1;
        int rightLength = r - m;
        // Create teo left and right temp arrays
        int left[] = new int[leftLength];
        int right[] = new int[rightLength];

        // Copy data to temp arrays from arr using l and m+1 as starting points
        for (int i = 0; i < leftLength; i++) {
            left[i] = arr[l + i];
        }
        for (int j = 0; j < rightLength; j++) {
            right[j] = arr[m + 1 + j];
        }

        // Merge the temp arrays using two pointers p1 and p2 and p as the pointer for the main array
        int p1 = 0, p2 = 0, p = l;
        while (p1 < leftLength && p2 < rightLength) {
            if (left[p1] < right[p2]) {
                arr[p++] = left[p1++];
            } else {
                arr[p++] = right[p2++];
            }
        }
        // Copy the remaining elements of left and right arrays to the main array
        if (p1 < leftLength) {
            for (int i = p1; i < leftLength; i++) {
                arr[p++] = left[i];
            }
        }
        if (p2 < rightLength) {
            for (int i = p2; i < rightLength; i++) {
                arr[p++] = right[i];
            }
        }

    }
    
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
        //Write your code here
        // If l >= r then return which means the array is of length 1 or 0 which is already sorted
        if (l >= r) {

            return;
        }
        // Find the middle point to divide the array into two halves
        int mid = (l + r) / 2;
        // Call mergeSort for first half
        sort(arr, l, mid);
        // Call mergeSort for second half
        sort(arr, mid + 1, r);
        
        // Merge the two halves sorted in step 2 and 3
        merge(arr, l, mid, r);

        //Call mergeSort from here 
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
  
        Exercise_4 ob = new Exercise_4(); 
        ob.sort(arr, 1, arr.length-1); 
  
        System.out.println("\nSorted array"); 
        printArray(arr); 
    } 
} 