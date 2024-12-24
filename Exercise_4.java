class MergeSort 
{
    // Time complexity: O(NlogN)
    // Space complexity: O(N)
    // Did this code successfully run on Leetcode : YES
    // Any problem you faced while coding this : No

    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int[] arr, int l, int m, int r)
    {
        //Your code here
        int[] temp = new int[r-l + 1];
        int leftPtr = l;
        int rightPtr = m + 1;

        int i = 0;
        while (leftPtr <= m && rightPtr <= r) {
            if (arr[leftPtr] <= arr[rightPtr]) {
                temp[i++] = arr[leftPtr++];
            } else {
                temp[i++] = arr[rightPtr++];
            }
        }

        while (leftPtr <= m) { // add remaining elements from left array
            temp[i++] = arr[leftPtr++];
        }

        while (rightPtr <= r) { // add remaining elements from right array
            temp[i++] = arr[rightPtr++];
        }

        for (int num: temp) { // copy temporary array to original array
            arr[l++] = num;
        }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int[] arr, int l, int r)
    { 
	    //Write your code here
        //Call mergeSort from here
        if (l >= r)   // base case: if at any moment low is equal to or greater than high, return
            return;

        int mid = l + (r - l)/2;
        // sort each halves
        sort(arr, l, mid); // first sorted array
        sort(arr, mid + 1, r); // second sorted array

        merge(arr, l, mid, r);
    } 
  
    /* A utility function to print array of size n */
    static void printArray(int[] arr)
    {
        for (int j : arr) System.out.print(j + " ");
        System.out.println(); 
    } 
  
    // Driver method 
    public static void main(String[] args)
    { 
        int[] arr = {12, 11, 13, 5, 6, 7};
  
        System.out.println("Given Array"); 
        printArray(arr); 
  
        MergeSort ob = new MergeSort(); 
        ob.sort(arr, 0, arr.length-1); 
  
        System.out.println("\nSorted array"); 
        printArray(arr); 
    } 
} 