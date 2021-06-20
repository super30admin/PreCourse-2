// Time Complexity : O(n log n)
// Space Complexity : O(n)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : I don't understand how to calculate time and space complexities :(

class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
       int size1 = m - l + 1;
       int size2 = r - m;

       //dummy arrays
       int left[] = new int[size1];
       int right[] = new int[size2];

       for(int  i = 0; i < size1; ++i){
           left[i] = arr[l + i];
       }
       for(int  j = 0; j < size2; ++j){
        right[j] = arr[m + 1 + j];
       }

       int i = 0;
       int j = 0;
       int k = l;

       while(i < size1 && j < size2){
           if(left[i] <= right[j]){
               arr[k] = left[i];
               i++;
           }
           else{
               arr[k] = right[j];
               j++;
           }
           k++;
       }

       while(i < size1){
           arr[k] = left[i];
           i++;
           k++;
       }

       while(j < size2){
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
    if(l < r){
        int m = l + (r - l)/2;
        sort(arr, l, m);
        sort(arr, m + 1, r);

        //Call mergeSort from here 
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