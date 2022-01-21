/**
Merge Sort - It's a devide & Conqure algorithm.

// Time Complexity :
    Sorting - Overall O(nlogn), where n is the length of an array. Time complexity for devide operation is O(logn) and merging will happen in linear time O(n).
// Space Complexity :
    Total space complexity = Auxilary space + space used towards input.
    original array O(n) where n is the length of an array + O(n/2) n/2 is length of first_array used for merging +
    O(n/2) n/2 is length of second_array used for merging.
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : No
**/
class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
        // 12, 11, 13, 5, 6, 7
        int fLength = (m-l) + 1;
        int sLength = r - m;
        int first_arra[] = new int[fLength];
        int second_arra[] = new int[sLength];
        
        for (int i=0; i<fLength; i++)
        {
            first_arra[i] = arr[l + i];
        }
        
        for (int i=0; i<sLength; i++)
        {
            second_arra[i] = arr[m + i + 1];
        }
        
        int fPtr = 0;
        int sPtr = 0;
        int outPtr = l;
        
        while (fPtr <fLength && sPtr < sLength)
        {
            if (first_arra[fPtr] <= second_arra[sPtr])
            {
                arr[outPtr] = first_arra[fPtr];
                fPtr++;
            }
            else if (first_arra[fPtr] > second_arra[sPtr])
            {
                arr[outPtr] = second_arra[sPtr];
                sPtr++;
            }
            outPtr++;
        }
        
        // transfer remaining elements from first_arra into the output array
        while (fPtr <fLength)
        {
            arr[outPtr] = first_arra[fPtr];
            fPtr++;
            outPtr++;
        }
        
        // transfer remaining elements from second_arra into the output array
        while (sPtr <sLength)
        {
            arr[outPtr] = second_arra[sPtr];
            sPtr++;
            outPtr++;
        }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
        if (l >= r)
        {
            return;
        }
        
	    int mid = l + (r - l) / 2;
        sort(arr, l, mid);
        sort(arr, mid + 1, r);
        merge(arr, l, mid, r);
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
        int arr[] = {12, 11, 13, -5, 6, 7, -4 ,1 ,8 ,-9 ,2 ,1}; 
  
        System.out.println("Given Array"); 
        printArray(arr); 
  
        MergeSort ob = new MergeSort(); 
        ob.sort(arr, 0, arr.length-1); 
  
        System.out.println("\nSorted array"); 
        printArray(arr); 
    } 
}