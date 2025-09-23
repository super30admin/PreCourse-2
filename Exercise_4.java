// Time Complexity: O(n log n) as we keep dividing the array into two halves.
// Space Complexity: O(n) as we use a temp array for sorting the elements.

class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int start, int mid, int right) 
    {  
       int i = start, j = mid;

       int[] temp = new int[right - start];
       int tempIdx = 0;
    
       while (i < mid && j < right) {
            if (arr[i] < arr[j]) {
                temp[tempIdx++] = arr[i++];
            } else {
                temp[tempIdx++] = arr[j++];
            }
       }

       while (i < mid) {
            temp[tempIdx++] = arr[i++];
       }

       while (j < right) {
            temp[tempIdx++] = arr[j++];
       }

       for(int k=start; k<right; k++) {
        arr[k] = temp[k-start];
       }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int start, int end) 
    { 
        if (end - start < 2) {
            return;
        }

        int mid = (start + end) / 2;
        sort(arr, start, mid);
        sort(arr, mid, end);

        merge(arr, start, mid, end);
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
        ob.sort(arr, 0, arr.length); 
  
        System.out.println("\nSorted array"); 
        printArray(arr); 
    } 
} 