// Time Complexity : O(nlog(n))
// Space Complexity : O(n)
// Did this code successfully run on Leetcode : no
// Any problem you faced while coding this : yes, how to decide on what to put in while

class MergeSort
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here
        int i = l;
        int j = m+1;
        int k=0;

        int newarray[] = new int[r-l+1];

        while(i<=m && j<=r)
        {
            if(arr[j]<arr[i])
            {
               newarray[k++] = arr[j++];
            }
            else
            {
                newarray[k++] = arr[i++];
            }
        }
        while(i<=m)
        {
            newarray[k++] = arr[i++];
        }
        while(j<=r)
        {
            newarray[k++] = arr[j++];
        }
        k=0;
        for(i=l; i<=r; i++)
        {
            arr[i] = newarray[k++];
        }
    }

    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    {
        if(l<r)
        {
            //Write your code here
            //Call mergeSort from here
            int m = l + (r-l)/2;
            sort(arr, l, m);
            sort(arr,m+1,r);
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