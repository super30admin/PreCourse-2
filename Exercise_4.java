// Time Complexity : O(n logn)
// Space Complexity : O(n) 
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : NO
class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
       int len1 = m - l + 1;
       int len2 = r-m;
       int L[] = new int [len1];
       int R[] = new int [len2];
       for(int i=0; i<len1;++i)
       {
        L[i]= arr[i+l];
       }
       for(int j=0;j<len2;++j)
       {
        R[j]=arr[m+1+j];
       }
       int i=0,j=0,k=l;

       while(i<len1&&j<len2){
        if((L[i]<=R[j])){
            arr[k]=L[i];
            i++;
        }
        else{
            arr[k]=R[j];
            j++;
        }
        k++;
       }
       while(i<len1){
        arr[k]=L[i];
        i++;
        k++;
       }
       while(j<len2){
        arr[k]=R[j];
        k++;
        j++;
       }

    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here 
        int m =(l+r)/2;
        if(l < r){
            sort(arr, l , m );
            sort(arr, m+1, r );
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