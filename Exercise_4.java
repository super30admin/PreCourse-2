// Did this code successfully run on Leetcode : It runs successfully on Eclipse
// Any problem you faced while coding this : Not much, other than coding for recursion in sort()

class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
    	 // Find sizes of two subarrays to be merged
        int size1 = m - l + 1;
        int size2 = r - m;
 
        /* Create temp arrays */
        int left[] = new int [size1];
        int right[] = new int [size2];
 
        /*Copy data to temp arrays*/
        for (int i=0; i<size1; ++i)
            left[i] = arr[l + i];
        for (int j=0; j<size2; ++j)
            right[j] = arr[m + 1+ j];
 
 
        /* Merge the temp arrays */
 
        // Initial indexes of first and second subarrays
        int i = 0, j = 0;
 
        // Initial index of merged subarray array
        int k = l;
        while (i < size1 && j < size2)
        {
            if (left[i] <= right[j])
            {
                arr[k] = left[i];
                i++;
            }
            else
            {
                arr[k] = right[j];
                j++;
            }
            k++;
        }
 
        /* Copy remaining elements of L[] if any */
        while (i < size1)
        {
            arr[k] = left[i];
            i++;
            k++;
        }
 
        /* Copy remaining elements of R[] if any */
        while (j < size2)
        {
            arr[k] = right[j];
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
    	  if (l < r)
          {
              // Find the middle point in array
              int mid = (l+r)/2;
   
              // Sort first and second halves seperately
              sort(arr, l, mid);
              sort(arr , mid+1, r);
   
              // Merge the sorted halves together
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
