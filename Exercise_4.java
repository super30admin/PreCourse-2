import java.util.Arrays;

// Time Complexity : O(n * log(n)). 
// Space Complexity :  O(n)  It requires the additional space as temporary array to merge two sub arrays.
// Did this code successfully run on Leetcode : 
// Any problem you faced while coding this :


// Your code here along with comments explaining your approach
class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
       int[] L = Arrays.copyOfRange(arr, l, m + 1);
       int[] R = Arrays.copyOfRange(arr, m + 1, r + 1);
       int i = 0, j = 0, a = l;
       while (i < L.length && j < R.length)
        {
            if (L[i] <= R[j])
            {
                arr[a] = L[i];
                i++;
            }
            else
            {
                arr[a] = R[j];
                j++;
            }
            a++;
        }

        while (i < L.length)
        {
            arr[a] = L[i];
            i++;
            a++;
        }

        while (j < R.length)
        {
            arr[a] = R[j];
            j++;
            a++;
        }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
        //Write your code here
        if(l < r) {
            int mid = (l + r) / 2;
            //Call mergeSort from here 
            sort(arr, l, mid);
            sort(arr, mid + 1, r);
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