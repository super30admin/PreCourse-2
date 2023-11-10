// Time Complexity : O(nlog n)
// Space Complexity : O(n)
// Did this code successfully run on Leetcode : no
// Any problem you faced while coding this :
import java.util.*;
class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int left[], int right[]) 
    {  
        int i = 0;
        int k = 0;
        int j = 0;

        while (i < left.length && j < right.length)
        {
            if(left[i] <= right[j])
            {
                arr[k] = left[i];
                i = i + 1;
            }
            else{
                arr[k] = right[j];
                j = j + 1;
            }
            k = k + 1;
        }

        while(i < left.length)
        {
            arr[k] = left[i];
            k = k + 1;
            i = i + 1;
        }
        
        while(j < right.length)
        {
            arr[k] = right[j];
            k = k + 1;
            j = j + 1;
        }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[]) 
    {
      int n = arr.length;
      if(n < 2)
          return;
      int mid = n/2;
      int left[] = new int[n/2];
      int right[] = new int[n - n/2];
      for(int i = 0; i < mid; i++)
        left[i] = arr[i];
          
      for(int i = mid; i < n; i++)
        right[i - mid] = arr[i];

      sort(left);
      sort(right);
      merge(arr, left, right);
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
        ob.sort(arr); 
  
        System.out.println("\nSorted array"); 
        printArray(arr); 
    } 
} 