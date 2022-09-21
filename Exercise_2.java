class QuickSort 
{ 
// Time Complexity : O(n log n)
// Space Complexity : O(1) n-> number of elemts present in array.
// Did this code successfully run on Leetcode :Yes
// Any problem you faced while coding this :No
     void swap(int arr[],int i,int j){
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;  
    }
    
    int partition(int arr[], int low, int high) 
    { 
        int pivot = arr[high];
    int i = (low-1);

    for (int j = low; j < high; j++) {
        if (arr[j] <= pivot) {
            i++;

            int swapTemp = arr[i];
            arr[i] = arr[j];
            arr[j] = swapTemp;
        }
    }

    int swapTemp = arr[i+1];
    arr[i+1] = arr[high];
    arr[high] = swapTemp;

    return i+1;
        
    } 
    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    void sort(int arr[], int low, int high) 
    {  
        if (low < high) {
            int partitionIndex = partition(arr, low, high);
    
            sort(arr, low, partitionIndex-1);
            sort(arr, partitionIndex+1, high);

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
