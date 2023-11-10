// Time Complexity : O(Nlog N)
// Space Complexity : O(N)
// Did this code successfully run on Leetcode : 
// Any problem you faced while coding this : No


// Your code here along with comments explaining your approach
//1. calculate mid index of array, call mergesort and recrusively call both left and right subarrays
//2. until it reaches single element, keep comparing left and right subarray
//3. merge all elements based on comparison from left and right subarray

class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
       //initialising size of both subarrays
       int len1 = m - l + 1;
       int len2 = r - m;
       int L[] = new int[len1];
       int R[] = new int[len2];
       for(int i = 0; i < len1; ++i){
           L[i] = arr[l+i];
       }
       for(int j = 0; j < len2; ++j){
           R[j] = arr[m+1+j];
       }
       int i = 0, j = 0;
       int k = l;
       while(i < len1 && j < len2){
           if(L[i] <= R[j]){
               arr[k] = L[i];
               i++;
           }
           else {
               arr[k] = R[j];
               j++;
           }
           k++;
       } 
       while(i < len1){
           arr[k] = L[i];
           i++;
           k++;
       }
       while(j < len2){
           arr[k] = R[j];
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
        if(l < r){
            int m = l + (r-1)/2;
            sort(arr, l, m);
            sort(arr, m+1, r);
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