class MergeSort {
    // Time Complexity : O(n log n)
    // Space Complexity : O(n)
    // Did this code successfully run on Leetcode : this problem is similar to 88. Merge Sorted Array
    // Any problem you faced while coding this : faced lil problem during merging

    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) {
       //Your code here
        // size of left and right side
        int sizeLeft = m-l+1; // min array size should be 1, so +1
        int sizeRight = r-m;

        // temp array
        // extra space
        int[] leftSide = new int[sizeLeft];
        int[] rightSide = new int[sizeRight];

        // copy data to temp array
        for(int i = 0; i < sizeLeft; i++)
            leftSide[i] = arr[i + l];

        for(int j = 0; j < sizeRight; j++)
            rightSide[j] = arr[j + m + 1]; // copy data from right side which starts from (mid+1)

        // start compare and merge
        int i=0; // size of leftSideArray
        int j=0;// size of rightSideArray
        int resultIndex = l;

        // compare each element and copy to main array
        while(i < sizeLeft && j < sizeRight){
            if(leftSide[i] > rightSide[j]){
                arr[resultIndex++] = rightSide[j++];
            } else {
                arr[resultIndex++] = leftSide[i++];
            }
        }

        // if we are still left with elements in any array copy them over to main array
        // left side
        for(;i < sizeLeft; i++){
            arr[resultIndex++] = leftSide[i];
        }

        // right side
        for(;j < sizeRight; j++){
            arr[resultIndex++] = rightSide[j];
        }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) {
	//Write your code here
        if(l < r) {
            int mid = (l + r - 1)/2; // calculate mid
            sort(arr, l, mid); // left side sort
            sort(arr, mid+1, r); // sort right side

            // Call mergeSort from here
            merge(arr, l, mid, r); // perform merge
        }

    } 
  
    /* A utility function to print array of size n */
    static void printArray(int arr[]) {
        int n = arr.length; 
        for (int i=0; i<n; ++i) 
            System.out.print(arr[i] + " "); 
        System.out.println(); 
    } 
  
    // Driver method 
    public static void main(String args[]) {
        int arr[] = {12, 11, 13, 5, 6, 7}; 
  
        System.out.println("Given Array"); 
        printArray(arr); 
  
        MergeSort ob = new MergeSort(); 
        ob.sort(arr, 0, arr.length-1); 
  
        System.out.println("\nSorted array"); 
        printArray(arr); 
    } 
} 