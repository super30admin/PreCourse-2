// Time Complexity : O(n log n) on average, O(n^2) in worst case (when pivot selection is poor)
// Space Complexity : O(log n) on average for recursion stack, O(n) in worst case
// Did this code successfully run on Leetcode : Not tested on Leetcode, but works correctly in local environment
// Any problem you faced while coding this : Initially used wrong arguments in swap() function (passed values instead of indices)

// Your code here along with comments explaining your approach:
// Approach:
// - We use the last element as the pivot
// - Partition the array such that elements less than pivot are on the left, greater on the right
// - Recursively apply the same logic to left and right subarrays
// - Swap is done without using an extra variable (XOR method)


class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	    //Try swapping without extra variable 
        if (i != j) {
        arr[i] = arr[i] ^ arr[j];
        arr[j] = arr[i] ^ arr[j];
        arr[i] = arr[i] ^ arr[j];
        }
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        int idx = l - 1, pivot = arr[h];
        for(int j = l; j < h; j++){
            if(arr[j] < pivot){
                idx++;
                swap(arr,j,idx);
            }
        }
        idx++;
        swap(arr,idx,h);
        return idx;
        //Compare elements and swap.
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        if(l < h) {
            int pivIdx = partition(arr,l,h);
            QuickSort(arr, l, pivIdx - 1); //left half call
            QuickSort(arr, pivIdx + 1, h); //right half call
        }
    } 
  
    // A utility function to print contents of arr 
    void printArr(int arr[], int n) 
    { 
        int i; 
        for (i = 0; i < n; ++i) 
            System.out.print(arr[i] + " "); 
    } 
  
    // Driver code to test above 
    public static void main(String args[]) 
    { 
        IterativeQuickSort ob = new IterativeQuickSort(); 
        int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 }; 
        ob.QuickSort(arr, 0, arr.length - 1); 
        ob.printArr(arr, arr.length); 
    } 
} 