// Time Complexity : O(nlog(n))
// Space Complexity : O(n)
// Did this code successfully run on Leetcode : N/A
// Any problem you faced while coding this : No

/*
In merge sort we divide the given array into the half continuously and keep swapping numbers in order to achieve
ascending order of elements, once the every array part is sorted, we then go for merging them together and get a
sorted array
 */
class MergeSort
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here
        int l1 = m - l + 1;
        int l2 = r - m;

        // Creating temporary arrays to save the data from the given array
        int temp1[] = new int[l1];
        int temp2[] = new int[l2];


        for (int i = 0; i < l1; ++i)
            temp1[i] = arr[l + i];
        for (int j = 0; j < l2; ++j)
            temp2[j] = arr[m + 1 + j];

        // iterating over the arrays and merging them together after comparing their values

        int i = 0, j = 0;

        int k = l;
        while (i < l1 && j < l2) {
            if (temp1[i] <= temp2[j]) {
                arr[k] = temp1[i];
                i++;
            }
            else {
                arr[k] = temp2[j];
                j++;
            }
            k++;
        }

        // appending all remaining elements in the arr from both temp1 and temp2 array
        while (i < l1) {
            arr[k] = temp1[i];
            i++;
            k++;
        }
        while (j < l2) {
            arr[k] = temp2[j];
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
        if(l<r){
            int mid = l + (r-l)/2;
            sort(arr, l, mid);
            sort(arr,mid+1, r);
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