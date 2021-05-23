//Time Complexity :O(nLogn) 
//Space Complexity : O(n) 
class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
        // Sizes of the 2 sub arrays to merge
        int s1 = m - l + 1;
        int s2 = r - m;
 
        int left[] = new int[s1];
        int right[] = new int[s2];
 
        for (int i = 0; i < s1; ++i)
            left[i] = arr[l + i];
        for (int j = 0; j < s2; ++j)
            right[j] = arr[m + 1 + j];
 
        //Merge 2 arrays
        int i = 0, j = 0;
 
        int k = l;
        while (i < s1 && j < s2) {
            if (left[i] <= right[j]) {
                arr[k] = left[i];
                i++;
            }
            else {
                arr[k] = right[j];
                j++;
            }
            k++;
        }
 
        // Copy remaining elements of left[] if any
        while (i < s1) {
            arr[k] = left[i];
            i++;
            k++;
        }
 
        // Copy remaining elements of right[] if any
        while (j < s2) {
            arr[k] = right[j];
            j++;
            k++;
        }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
    	 if (l < r) {
            // Find the middle index
            int m =l+(r-l)/2;
 
            // Sort first and second halves
            sort(arr, l, m);
            sort(arr, m + 1, r);
 
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