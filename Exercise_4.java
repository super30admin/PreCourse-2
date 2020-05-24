// Time Complexity : O(nlogn) (n is the array size) Each step half of the array is discarded so n * logn
// Space Complexity : O(n) (arrray size)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : Yes, in merge method


class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
        int a1 = m-l+1; // lenght of array from low to mid half of array
       int a2 = r - m; // length of array from mid to high
       
       int arr1[] = new int[a1];
       int arr2[] = new int[a2];
       
       for (int i = 0; i < a1 ; i++) { // copy first half (sorted) of elements to arr1
           arr1[i] = arr[l+i];
       }
       for(int j = 0; j < a2 ; j++) { // copy second half (sorted) of elements to arr2
           arr2[j] = arr[m+1+j]; 
       }
       
       int i = 0, j = 0, k = l;
       
       while(i < a1 && j < a2) { // boundary condition for i and j wrt array size
           
           if (arr1[i] < arr2[j]) { // compare the values of arr1 and arr2 and copy the smaller value to arr
               arr[k] = arr1[i];
               i++;
               k++;
           }
           else {
               arr[k] = arr2[j]; 
               j++;
               k++;
           }
       }
       
       while (i < a1) { // if only arr1 elements remaining copy to arr
           arr[k] = arr1[i];
           i++;
           k++;
       }
       
       while (j < a2) { // if only arr2 elements remaining copy to arr
           arr[k] = arr2[j];
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
        if(l<r) { 
        int mid = l + (r-l)/2; // find mid for partition
        sort(arr,l,mid); // continue to single elements
        sort(arr,mid+1,r);
        merge(arr,l,mid,r); // call merge method
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