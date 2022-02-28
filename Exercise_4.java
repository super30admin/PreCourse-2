
/*
Time Complexity : O(nlogn) DnC approach.
Space Complexity : O(n) but additional of O(n) hile procecessing

Did this code successfully run on Leetcode :
Finished in 78 ms
Given Array
12 11 13 5 6 7 

Sorted array
5 6 7 11 12 13 

Any problem you faced while coding this :
none.

Your code here along with comments explaining your approach :
Straight forward approach
*/
class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       int size1 = m - l + 1;
       int size2 = r - m;
       int[] leftArr = new int[size1];
       int[] rightArr = new int[size2];

        for (int i = 0; i < size1; ++i)
            leftArr[i] = arr[l + i];
        for (int j = 0; j < size2; ++j)
            rightArr[j] = arr[m + 1 + j];

        int i = 0;
        int j = 0;
        int k = l;
        while (i < size1 && j < size2) {
            if (leftArr[i] <= rightArr[j]) {
                arr[k] = leftArr[i];
                i++;
            }
            else {
                arr[k] = rightArr[j];
                j++;
            }
            k++;
        }
        while (i < size1) {
            arr[k] = leftArr[i];
            i++;
            k++;
        }
  
        while (j < size2) {
            arr[k] = rightArr[j];
            j++;
            k++;
        }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
        //Call mergeSort from here 
        if(l < r){
            int mid = (l + r) / 2;
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