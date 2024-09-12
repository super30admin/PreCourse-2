// Time Complexity : O(nlogn)
// Space Complexity :  O(n)
// Did this code successfully run on Leetcode : No
// Any problem you faced while coding this : No

class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  

       int bufferSize = r-l+1;
       int[] buffer = new int[bufferSize];
       int lp = l;
       int rp = m+1;
       int t=0;

       while(lp<=m && rp<=r){
           if(arr[lp]<arr[rp]){
               buffer[t] = arr[lp];
               t = t+1;
               lp = lp+1;
           }else{
               
               buffer[t] = arr[rp];
               t = t+1;
               rp = rp+1;
           }
        }

       while(lp<=m){
           buffer[t] = arr[lp];
           t = t+1;
           lp = lp+1;
       }
       while(rp<=r){
           buffer[t] = arr[rp];
           t = t+1;
           rp = rp+1;
       }

       for(int i=l;i<=r;i++){
           arr[i] = buffer[i-l];
       }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here 

        if(l==r){
            return;
        }else{
            int mid = l+(r-l)/2;
            sort(arr, l, mid);
            sort(arr, mid+1, r);
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