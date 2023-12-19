// TC: O(N log N)
class MergeSort
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       int n1 = m - l + 1;
       int n2 = r - m;
       int start1 = l;
       int start2 = m + 1;
       int[] left = new int[n1];
       int[] right = new int[n2];

       for (int i = 0; i < n1; i++) {
           left[i] = arr[start1 + i];
       }
       for (int i = 0; i < n2; i++) {
           right[i] = arr[start2 + i];
       }
       int leftPointer = 0, rightPointer = 0, resPointer = l;

       while (leftPointer < n1 && rightPointer < n2) {
           if (left[leftPointer] <= right[rightPointer]) {
               arr[resPointer] = left[leftPointer];
               leftPointer++;
           } else {
               arr[resPointer] = right[rightPointer];
               rightPointer++;
           }
           resPointer++;
       }
       while (leftPointer < n1) {
           arr[resPointer++] = left[leftPointer++];
       }
       while (rightPointer < n2) {
           arr[resPointer++] = right[rightPointer++];
       }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
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