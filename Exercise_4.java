// Time Complexity : O(nlogn)
// Space Complexity :O(n)
// Did this code successfully run on Leetcode : n/a
// Any problem you faced while coding this : no

// Your code here along with comments explaining your approach
class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here 
       int i = 0; 
       int j = 0; 
       int n1 = m - l + 1;
       int n2 = r - m;

       int arr_l[] = new int [n1];
       int arr_r[] = new int [n2];

       for ( i =0; i<n1; ++i)
           arr_l[i] = arr[l + i];
       for (j =0; j<n2; ++j)
           arr_r[j] = arr[m + 1+ j];

      i=0;
      j=0;

       int k = l;
       while (i < n1 && j < n2)
       {
           if (arr_l[i] <= arr_r[j])
           {
               arr[k] = arr_l[i];
               i++;
           }
           else
           {
               arr[k] = arr_r[j];
               j++;
           }
           k++;
       }

       while (i < n1)
       {
           arr[k] = arr_l[i];
           i++;
           k++;
       }

       while (j < n2)
       {
           arr[k] = arr_r[j];
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
            int mid = (l+r)/2;

            sort(arr, l, mid);
            sort(arr , mid+1, r);
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
