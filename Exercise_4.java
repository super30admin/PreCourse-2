// Time Complexity : Dont know
// Space Complexity : Dont know
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : Understanding the algorithm took some time. Also Complexities.

class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
        int len1 = m - l + 1;
        int len2 = r - m;
        
        int a[] = new int[len1];
        int b[] = new int[len2];
        
        for(int i=0; i<len1; i++){
            a[i] = arr[l + i];
        }
        for(int j=0; j<len2; j++){
            b[j] = arr[m + 1 + j];
        }
        
        int i = 0;
        int j = 0;
        int k = l;
        while(i < len1 && j < len2){
            if(a[i] <= b[j]){
                arr[k] = a[i];
                i++;
            }
            else{
                arr[k] = b[j];
                j++;
            }
            k++;
        }
        while(j < len2){
            arr[k] = b[j];
            j++;
            k++;
        }
        while(i < len1){
            arr[k] = a[i];
            i++;
            k++;
        }
       
    } 
  
 
    void sort(int arr[], int l, int r) 
    { 
        if(l < r){
            int mid = l + (r-l)/2;
            sort(arr,l,mid);
            sort(arr,mid+1,r);
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

        MergeSort ob = new MergeSort(); 
        ob.sort(arr, 0, arr.length-1); 
  
        System.out.println("\nSorted array"); 
        printArray(arr); 
    } 
} 