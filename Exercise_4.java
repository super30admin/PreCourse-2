// Time Complexity : O(n logn)
// Space Complexity : O(n)
// Did this code successfully run on Leetcode :
// Any problem you faced while coding this : NO

class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       int n1 = m-l+1;
       int n2 = r-m;
       // Creating temp arrays to store 
       int[] arr1 = new int[n1];
       int[] arr2 = new int[n2];

       // Initializing temp arrays
       for(int i =0; i< n1; i++){
           arr1[i] = arr[i+l];
       }
       for(int i =0; i< n2; i++){
           arr2[i] = arr[i+m+1];
       }

       // i keep track of array1 and j keep track of array2
       int i = 0;
       int j = 0;
  
        // index keep track of original array
        int index = l;

        //Merge arrays
        while (i < n1 && j < n2) {
            if (arr1[i] <= arr2[j]) {
                arr[index] = arr1[i];
                i++;
            }
            else {
                arr[index] = arr2[j];
                j++;
            }
            index++;
        }

        //Copy remaining elements of temp arrays
        while (i < n1) {
            arr[index] = arr1[i];
            i++;
            index++;
        }
        while (j < n2) {
            arr[index] = arr2[j];
            j++;
            index++;
        }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here 
        if(l < r){
            int midIndex = l + (r - l) /2;
            sort(arr, l, midIndex);
            sort(arr, midIndex+1, r);

            merge(arr, l, midIndex, r);
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