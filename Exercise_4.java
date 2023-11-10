// Time Complexity : O(m+n)
// Space Complexity : O(nlogn)
// Did this code successfully run on Leetcode : Yes - Used IntelliJ
// Any problem you faced while coding this : I was not aware of the concept before, so went through it

class MergeSort
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {
        int len1 = (m-l)+1;
        int len2 = (r-m);
        int L[] = new int[len1];
        int R[] = new int[len2];
        for(int i=0;i<len1;i++) {
            L[i] = arr[l+i];
        }
        for(int j=0;j<len2;j++) {
            R[j] = arr[m+j+1];
        }
        int p=0;
        int q=0;
        int s=l;
        while(p<len1 && q<len2) {
            if(L[p]<=R[q]) {
                arr[s++] = L[p++];
            } else {
                arr[s++] = R[q++];
            }
        }
        while(p<len1) {
            arr[s++] = L[p++];
        }
        while(q<len2) {
            arr[s++] = R[q++];
        }
    }
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r)
    {

	//Write your code here
        //Call mergeSort from here
        if(l<r) {
            int m = (int)Math.floor((l+r)/2);
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