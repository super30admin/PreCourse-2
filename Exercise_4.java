// Time Complexity : O(n log n)
// Space Complexity : O(n)
// Did this code successfully run on Leetcode : -
// Any problem you faced while coding this : -

class MergeSort
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here
        int n1 = m - l +1;
        int n2= r - m;
        
        /*Create two temp arrays to hold the left and right arrays
         * Populate them using the input array
         * */
        int[] leftArr = new int[n1];
        int[] rightArr = new int[n2];

        for (int i = 0; i < n1; ++i){
            leftArr [i] = arr[l+i];}

        for (int j = 0; j < n2; ++j){
            rightArr [j] = arr[m+1+j];}

        //Merge temp arrays
        int i=0;
        int j=0;

	   int k = l;
	   while(i < n1 && j < n2)
	   {
	       if (leftArr[i] < rightArr[j]){
	           arr[k] = leftArr[i];
	           i++;
	       }
	       else {
	           arr[k] = rightArr[j];
	           j++;
	       }
	       k++;
	   }
	    while (i< n1)
	    {
	        arr[k] = leftArr[i];
	        i++;
	        k++;
	    }
	    while (j< n2)
	    {
	        arr[k] = rightArr[j];
	        j++;
	        k++;
	        }

    }
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) {
        //Write your code here
        if (l<r) {
            int mid = (l+r)/2;

            sort(arr, l, mid);
            sort(arr, mid + 1, r);
            //Call mergeSort from here
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