// Time Complexity : O(NlogN)
// Space Complexity :O(N) using extra space for the array.
// Did this code successfully run on Leetcode : No, ran it on the editor
// Any problem you faced while coding this : No
class MergeSort
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here
        //get the size for both the arrays
        int left_arr_size  = m-l+1;
        int right_arr_size = r-m;
        //create arrays for left and right subarray
        int []left_arr = new int[left_arr_size];
        int []right_arr = new int[right_arr_size];

        //copy 2 sorted sub arrays in left and right array
        for (int i = 0; i < left_arr_size; i++) {
            left_arr[i] = arr[l+i];
        }

        for (int i = 0; i < right_arr_size ; i++) {
            right_arr[i] = arr[m+1+i];
        }
        int i = 0, j = 0;
        /* to keep track of index of the new sorted array..start if from the left value.*/
        int k = l;
        while (i < left_arr_size && j < right_arr_size) {
            if (left_arr[i] <= right_arr[j]) {
                arr[k] = left_arr[i];
                i++;
            } else {
                arr[k] = right_arr[j];
                j++;
            }
            k++;
        }

        //copy whatever is left from both arrays
        while (i < left_arr_size) {
            arr[k] = left_arr[i];
            i++;
            k++;
        }
        while (j < right_arr_size) {
            arr[k] = right_arr[j];
            j++;
            k++;
        }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here
        if (l < r) {
            int middle = l + (r-l)/2;

            sort(arr, l, middle);
            sort(arr, middle +1, r);

            merge(arr, l, middle, r);
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