// Time Complexity : Need to refresh my knowledge on this.
// Space Complexity : Need to refresh my knowledge on this.
// Did this code successfully run on Leetcode : YES(Over local ide)..
// Any problem you faced while coding this : None, other than t.c and s.c.
class QuickSort
{ 
    /* This function takes last element as pivot, 
       places the pivot element at its correct 
       position in sorted array, and places all 
       smaller (smaller than pivot) to left of 
       pivot and all greater elements to right 
       of pivot */
    void swap(int arr[],int i,int j){
        //Your code here
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
    
    int partition(int arr[], int low, int high) 
    { 
   	//Write code here for Partition and Swap
        //choose any element from the array for pivot.
        int pivot = arr[high];
        //index from where we're going to swap the values with.
        int iIndex = low-1;
        //loop until we reach to the last index.
        for(int j = low; j < high; j++){
            //all the values lower than pivot should be to the left side.
            if(arr[j] < pivot){
                //only increment if the current element at j is less than pivot.
                iIndex++;
                //swap the values at i and j index.
                swap(arr,iIndex,j);
            }
        }
        //post the loop is completed, now the current i index will be at last swapped value and pivot is greater than that so we
        //increment the i index and swap with high as high contains the pivot
        iIndex++;
        swap(arr,iIndex,high);
        return iIndex;
    } 
    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    void sort(int arr[], int low, int high) 
    {  
            // Recursively sort elements before 
            // partition and after partition
        if(low < high) {
            int indexOfPartition = partition(arr, low, high);
            //sort the element on left side of partition and right side too.
            sort(arr, low, indexOfPartition - 1);
            sort(arr, indexOfPartition + 1, high);
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
