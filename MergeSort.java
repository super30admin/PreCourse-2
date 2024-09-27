// Time Complexity : For all cases, θ(n log n)
// Space Complexity : O(n)
// Any problem you faced while coding this : No

class MergeSort
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       // To get the size of two subarrays to be merged
       int size1 = m - l + 1;
       int size2 = r - m;

       // To create temporary arrays
        int left[] = new int[size1];
        int right[] = new int[size2];

        for(int i=0; i < size1; ++i) {
            left[i] = arr[l+i];
        }
        for(int j=0; j < size2; ++j) {
            right[j] = arr[m+1+j];
        }
        // Merging temporary arrays
        int i=0, j=0;

        int k=l;
        while(i < size1 && j < size2) {
            if(left[i] <= right[j]) {
                arr[k] = left[i];
                i++;
            } else {
                arr[k] = right[j];
                j++;
            }
            k++;
        }
        // Copying remaining elements of left[] is there are any
        while(i < size1) {
            arr[k] = left[i];
            i++;
            k++;
        }
        // Copying remaining elements of right[] is there are any
        while(j < size2) {
            arr[k] = right[j];
            j++;
            k++;
        }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	    if(l < r){
	        // Find middle point
            int m = l+(r-l)/2;

            // Sorting first and second halves
            sort(arr, l, m);
            sort(arr, m+1, r);

            // Merge the sorted halves
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