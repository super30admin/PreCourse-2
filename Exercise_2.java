// Time Complexity : O(n log n)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode :
// Any problem you faced while coding this : NO

class QuickSort 
{ 
    
    void swap(int arr[],int i,int j){
        // In first value, we store sum of two values
        arr[i] = arr[i] + arr[j];
        //In Second value, we are subtracting second value from the sum so it results in first value
        arr[j] = arr[i] - arr[j];
        //In First value, we are subtracting first value from the sum so it results in second value
        arr[i] = arr[i] - arr[j];
    }

    /* This function takes last element as pivot, 
       places the pivot element at its correct 
       position in sorted array, and places all 
       smaller (smaller than pivot) to left of 
       pivot and all greater elements to right 
       of pivot */
    
    int partition(int arr[], int low, int high) 
    {
        int pivot = high;
        high--;
        while(low <= high){
            //while value at left is less than pivot move low towards right
            if(arr[low] < arr[pivot]){
                low++;
            }
            //while value at right is greater than pivot move high towards left
            else if(arr[high] > arr[pivot]){
                high--;
            }
            // if both step 1 and step 2 does not match swap left and right
            else{
                swap(arr, low, high);
            }
        }
        //Move pivot to its correct position, if it is not in the correct position
        if (low != pivot)
            swap(arr, low, pivot);
        
        return low;
    } 
    
    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    void sort(int arr[], int low, int high) 
    {
        if(low < high){
            //Finding the partition point
            int partition = partition(arr, low, high);
            //Sorting left subarray to the partition
            sort(arr, low, partition-1);
            //Sorting Rigth subarray to the partition
            sort(arr, partition+1, high);
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
