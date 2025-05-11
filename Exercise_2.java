class QuickSort 
{ 
    // Time Complexity : O(nlogn) -> most of the cases (O(n^2) in real worst cases like wrong pivot chosen)
    // Space Complexity : O(log n) -> recursive calls stack (O(n) if worst pivot chose, completely imbalanced tree)
    // Did this code successfully run on Leetcode : Yes
    // Any problem you faced while coding this : took time to understand it and brush up again properly
    
    
    /* This function takes last element as pivot, 
       places the pivot element at its correct 
       position in sorted array, and places all 
       smaller (smaller than pivot) to left of 
       pivot and all greater elements to right 
       of pivot */

    void swap(int arr[],int i,int j){
        //Your code here
	// need to apply this logic otherwise it can lead to zero
	if (i != j) {
        arr[i] = arr[i] + arr[j];
        arr[j] = arr[i] - arr[j];
        arr[i] = arr[i] - arr[j];
    }
    }
    
    int partition(int arr[], int low, int high) 
    { 
   	//Write code here for Partition and Swap 
    //Compare elements and swap.
        int idx = low-1;
        int pivot = arr[high];
        for(int j = low;j<high;j++){
            if(arr[j]<=pivot){
                idx++;
                //swapping the smaller number to left
                swap(arr, j, idx);
            }
        }
        idx++;
        //swapping the pivot
        swap(arr, high, idx);
        return idx;
    } 
    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    void sort(int arr[], int low, int high) 
    {  
            // Recursively sort elements before 
            // partition and after partition 
        if (low < high) {
        int pidx = partition(arr, low, high);

        sort(arr, low, pidx - 1);
        sort(arr, pidx + 1, high);
        }
    } 
  
    /* A utility function to print array of size n */
    static void printArray(int arr[]) 
    { 
        int n = arr.length; 
        for (int i=0; i<n; ++i) 
            System.out.print(arr[i]+" "); 
        System.out.println(); 
    } 
  
    // Driver program 
    public static void main(String args[]) 
    { 
        int arr[] = {10, 7, 8, 9, 1, 5}; 
        int n = arr.length; 
  
        QuickSort ob = new QuickSort(); 
        ob.sort(arr, 0, n-1); 
  
        System.out.println("sorted array"); 
        printArray(arr); 
    } 
} 
