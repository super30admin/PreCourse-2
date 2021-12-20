// Time Complexity : O(N log N)
// Space Complexity :O(N) - extra spac etaken by the array used for the merge operation
// Did this code successfully run on Leetcode : N/A
// Any problem you faced while coding this : N/A


class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
       int result[] = new int[r-l+1];
       System.out.println(l +", "+ m +", "+ r);
       int i = l;
       int j = m+1;
       int k=0;

       while(i<=m && j <= r)
       {
            if(arr[i] <= arr[j])
            {
                result[k]= arr[i];
                i++;
                k++;
            }
            else
            {
                result[k] = arr[j];
                j++;
                k++;
            }
       }

       while( i <= m)
       {
            result[k] =arr[i];
            i++;
            k++;

       }

       while(j <= r)
       {
           result[k]= arr[j];
           j++;
           k++;
       }

       for(int index =l; index<=r; index++)
       {
            arr[index]= result[index-l];
       }  
     } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
        //Write your code here
        if( l< r)
        {
            int m = l + (r-l)/2;
            sort(arr, l, m);
            sort(arr, m+1, r);
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