// Time Complexity : O(n log(n))
// Space Complexity : O(n)
// Did this code successfully run on Leetcode :
// Any problem you faced while coding this : No

class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {
        //Your code here
        // copy left & right array
        int leftArrLen = m - l + 1;
        int rightArrLen = r - m;

        int leftArr[] = new int[leftArrLen];
        int rightArr[] = new int[rightArrLen];

        for (int i = 0; i < leftArrLen; i++) {
            leftArr[i] = arr[l+i];
        }

        for (int j = 0; j < rightArrLen; j++) {
            rightArr[j] = arr[m+1+j];
        }
    
        int i = 0;
        int j = 0;
        int k = l;

        while (i < leftArrLen && j < rightArrLen) {
            if (leftArr[i] <= rightArr[j]){
                arr[k] = leftArr[i];
                i++;
            } 
            else {
                arr[k] = rightArr[j];
                j++;
            }
            k++;
        }

        while (i < leftArrLen) {
            arr[k] = leftArr[i];
            i++;
            k++;
        }

        while (j < rightArrLen) {
            arr[k] = rightArr[j];
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

        if (l < r) {
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