// Time Complexity : O(NlogN)
// Space Complexity : O(N). Space used for leftHalf and rightHalf arrays.
// Did this code successfully run on Leetcode : No, did not find it on Leetcode.
// Any problem you faced while coding this : Yes, I had to watch some youtube videos to recollect merge sort.
class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
        int leftSize = m - l + 1; // Since arr is 0 indexed, used "+ 1" to get the correct size.
        int rightSize = r - m; // m index is already included in the leftSize, so no need of "+ 1" here.
        int[] leftHalf = new int[leftSize];
        int[] rightHalf = new int[rightSize];
        // Copy left half of arr into leftHalf[]
        for (int x = 0; x < leftSize; x++) {
            leftHalf[x] = arr[l + x];
        }
        // Copy right half of arr into rightHalf[]
        for (int i = 0; i < rightSize; i++) {
            rightHalf[i] = arr[m + 1 + i];
        }
        int i = 0; // index to iterate through leftHalf[]
        int j = 0; // index to iterate through rightHalf[]
        int k = l; // index to iterate through arr
        // Compare elements in leftHalf with rightHalf and add in the ascending order in arr.
        // Note that the leftHalf and rightHalf are already sorted subarrays.
        while (i < leftSize && j < rightSize) {
            if (leftHalf[i] <= rightHalf[j]) {
                arr[k ++] = leftHalf[i ++];
            } else {
                arr[k ++] = rightHalf[j ++];
            }
        }

        // Add the remaining elements from left partition to arr, which is already sorted.
        while (i < leftSize) {
            arr[k ++] = leftHalf[i ++];
        }
        // Add the remaining elements from right partition to arr, which is already sorted.
        while (j < rightSize) {
            arr[k ++] = rightHalf[j ++];
        }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        if (l < r) {
            int m = (l + r) / 2; // find mid
            // Keep partitioning the left subarray in a recursive way and then merge by sorting.
            sort(arr, l, m);
            // Keep partitioning the right subarray in a recursive way and then merge by sorting.
            sort(arr, m + 1, r);
            //Call mergeSort from here 
            // Merge left and right partitions/subarrays in ascending order of the elements.
            merge(arr, l, m, r);
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