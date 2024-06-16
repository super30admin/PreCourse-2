// Time Complexity : Problem need to be solved with Stack ADT 
// Space Complexity : Problem need to be solved with Stack ADT 
// Did this code successfully run on Leetcode : No
// Any problem you faced while coding this : Yes, Could not understand how to implement quicksort using Stack data structure. Help will be appreciated.


// Your code here along with comments explaining your approach

// Swap: just add and subtract the given values
// Partition: Same as Recursive QuickSort
// Quicksort using Stack ADT need to be done






class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
        if(i!=j){
            arr[i] = arr[i] + arr[j];
            arr[j] = arr[i] - arr[j];
            arr[i] = arr[i] - arr[j];
        }
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
        int pivot=h;
        while(l<h)
        {
            while(arr[l]<arr[pivot])
            {
                l++;
            }
            while(arr[h]>arr[pivot])
            {
                h--;
            }
            if(l<h){
                swap(arr,l,h);
            }
        }
        swap(arr,l,pivot);
        return l;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.


        // I cannot understand how to do this using stack
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