// Time Complexity : O(NLOGN)
// Space Complexity : O(N)
// Did this code successfully run on Leetcode :
// Any problem you faced while coding this :


class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
    	
        // Find sizes of two subarrays to be merged
        int left_length = m - l + 1;
        int right_length = r - m;
 
       
        int[] leftarray = new int[left_length];
        int[] rightarray = new int[right_length];
 
   
        for (int i = 0; i < left_length; ++i)
        	leftarray[i] = arr[l + i];
        for (int j = 0; j < right_length; ++j)
        	rightarray[j] = arr[m + 1 + j];
 
    
 
        // Initial indexes of first and second subarrays
        int left = 0, right = 0;
 
        // Initial index of merged subarray array - start from l 
        int curr = l;
        while (left < left_length && right < right_length) {
            if (leftarray[left] <= rightarray[right]) {
                arr[curr++] = leftarray[left++]; 
            }
            else {
                arr[curr++] = rightarray[right++];   
            }
        
        }
 
        while (left < left_length) {
            arr[curr++] = leftarray[left++];
        }
 
        while (right < right_length) {
            arr[curr++] = rightarray[right++];
        }
    }
  
    // Main function that sorts arr[l..r] using 
    // merge() 
     
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here
    	if (l < r) {
    		int mid = l+(r-l)/2;
    		sort(arr, l , mid);
    		sort(arr, mid+1, r);
    		merge(arr, l , mid, r);
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