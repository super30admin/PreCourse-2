
// Time Complexity : O(nlogn)
// Space Complexity :O(n)
// Did this code successfully run on Leetcode :
// Any problem you faced while coding this :


// Your code here along with comments explaining your approach

class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[],int l, int mid , int r) 
    {  
   
      int len1 = mid-l+1;
      int len2 = r-mid;
      int[] arr1 = new int[len1];
      
      int[] arr2 = new int[len2];
      int m = 0;
      int n = 0;
      int k = l;
    for(int i =0; i<len1;i++){
        arr1[i]=arr[i+l];
    }
    for(int i =0; i<len2;i++){
        arr2[i]=arr[mid+i+1];
    }

      while(m<len1 && n<len2){
        if(arr1[m]<= arr2[n]){
            arr[k++] = arr1[m++];
        } else {
            arr[k++]=arr2[n++];
        }
      }
       while(m<len1){
        arr[k++] = arr1[m++];
       }
       while(n<len2){
        arr[k++]=arr2[n++];       
       }
      
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
        if(l<r){
            
        int mid = l + (r-l)/2;

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
/*
 * Output
 * Given Array
12 11 13 5 6 7 

Sorted array
5 6 7 11 12 13 
 */
