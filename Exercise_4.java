// Time Complexity : O(n log n) -> logn to divide arrays into halves and n for merging halves
// Space Complexity : O(n) -> due to use of temp arrays
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : No problems faced

// Your code here along with comments explaining your approach

class MergeSort
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here
        //calculating sizes of 2 subarrays
        int nl = m - l + 1;
        int nr = r - m;

        //creating temp arrays since we are inplace sorting
        int lArr[] = new int[nl];
        int rArr[] = new int[nr];

        //copying data to temp arrays so that we can compare and merge those values in main arr
        for(int i = 0; i < nl; i++) {
            lArr[i] = arr[l + i];
        }
        for(int i = 0; i < nr; i++) {
            rArr[i] = arr[m + 1 + i];
        }

        //merge temp arrays which are sorted, use merge 2 sorted arrays logic
        int i = 0, j = 0;   //iterators for nArr and rArr
        //index to replace in main input subarray
        int k = l;
        while(i < nl && j < nr) {
            if(lArr[i] <= rArr[j]) {
                arr[k] = lArr[i];   //left has smaller so that is added and i incremented
                i++;
            } else {
                arr[k] = rArr[j];   //right has smaller no so that is added and j incremented
                j++;
            }
            k++;
        }

        //copy if any elements remaining in lArr
        while(i < nl) {
            arr[k] = lArr[i];
            i++;
            k++;
        }

        //copy if any elements remaining in rArr
        while(j < nr) {
            arr[k] = rArr[j];
            j++;
            k++;
        }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here
        if(l < r) {
            int mid = l + (r - l) / 2;
            //call sort recursively on left half array
            sort(arr, l, mid);
            //call sort recursively on right half array
            sort(arr, mid + 1, r);
            //merge sorted arrays
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