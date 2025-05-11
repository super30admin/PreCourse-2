// Time Complexity : O(n log n) -> divides array into half[log n] + marge each array [O(n)]
// Space Complexity : O(n) -> temp arrays L[] and R[] created for each merge
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : Spent time reviewing and revising concept
class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       int len1 = m - l +1;
       int len2 = r - m;

       int L[] = new int[len1];     //length of two subarrays
       int R[] = new int[len2];

       for(int i=0; i<len1; i++)    //copy data to temp arrays
            L[i] = arr[l+1];
        for(int j=0; j<len2; j++)
            R[j] = arr[m+1+j]

        int i=0, j=0;   //merge temp arrays
        int k = l;
        while(i < len1 && j < len2) {
            if(L[i] <=R[j]) {
                arr[k] = L[i];
                i++;
            }
            else {
                arr[k] = R[j];
                j++;
            }
            k++;
        }

        while(i < len1){    //copy remaining elements from L[] if any
            arr[k] = L[i];
            i++;
            k++;
        }

        while(j < len2){    //copy remaining elements from R[] if any
            arr[k] = R[j];
            j++;
            k++;
        }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
        if(l < r) {
             int mid = l+(r-l)/2;

             sort(arr, l ,mid); // sorts first half
             sort(arr, mid+1, r) // sorts second half

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