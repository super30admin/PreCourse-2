//Time Complexity: O(N log N)
//Space Complexity: O(1)
// Did this code successfully run on Leetcode : YES
// Any problem you faced while coding this : NO

class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //calculate left subarray size and right
       int length1 = m - l + 1;
       int length2 = r - m;

       int left[] = new int[length1];
       int right[] = new int[length2];

       // we put the data to left and right sub array
       for (int i = 0; i < length1; ++i)
           left[i] = arr[l + i];
       for (int j = 0; j < length2; ++j)
           right[j] = arr[m + 1 + j];


       // Initailize the Index of left and right sub array
       int i = 0, j = 0;

       // Initialize the index k of merged array
       int k = l;
       while (i < length1 && j < length2) {
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

       // we copy remaining left over elements of left array
       while (i < length1) {
           arr[k] = left[i];
           i++;
           k++;
       }

      //Similarly for the right array
       while (j < length2) {
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
        if (l < r) {

           //middle
            int m = l + (r - l) / 2;
           
            sort(arr, l, m); //sorted first half
            sort(arr, m + 1, r); //sorted second half
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