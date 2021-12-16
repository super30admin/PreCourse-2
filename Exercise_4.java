/*
 Time complexity: O(NlogN) where N is size of array.
 Scpace complexity: O(N) to maintaing the call recursive call stack
 Did this code successfully run on Leetcode : Yes
 Any problem you faced while coding this : Yes, i had to brushup merge sort algorithm
*/

class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
       int[] tempArr = new int[r - l + 1];
       int i = l, j = m + 1, pos = 0;

       while(i <= m && j <= r && pos < tempArr.length){
           if(arr[i] < arr[j]){
               tempArr[pos++] = arr[i++];
           }else{
               tempArr[pos++] = arr[j++];
           }
       }

       //below while loop will handle cases when either of i or j reaches it's end
       while(i <= m){
        tempArr[pos++] = arr[i++];
       }
       while(j <= r ){
        tempArr[pos++] = arr[j++];
       }
       
       //we copy sorted value to the actual array space
       pos = l;
       for(i = 0; i < tempArr.length; i++){
            arr[pos++] = tempArr[i];
        }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here 
        if(l < r){
            // more than one elements in current array space
            // split the array space into two from middle and call sort function on them
            int mid = l + (r - l)/2;
            sort(arr, l, mid); // perform sort operation on half of array
            sort(arr, mid + 1, r); // perform sort operarion on other half of array
            
            // after sort function returns, we have two arrays space which are sorted among them
            // we need to merge two sorted array
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