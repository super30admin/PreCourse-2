/**
Quick Sort - It's a devide & Conqure algorithm.
// Time Complexity :
    Sorting - in the worst case O(n^2) where n is the length of an array. It occurs if the partiion process picks every time the largest element as pivot. Best case O(nlogn) where n is the length of an array. It occurs when the partition process every time picks the median as the pivot from the array.  
// Space Complexity :
    Total space complexity = Auxilary space + space used towards input.
    O(n) in worst case and O(logn) for best case. where n is the length of an array.
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : No
**/
class QuickSort 
{ 
    /* This function takes last element as pivot, 
       places the pivot element at its correct 
       position in sorted array, and places all 
       smaller (smaller than pivot) to left of 
       pivot and all greater elements to right 
       of pivot */
    void swap(int arr[],int i,int j){
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
    
    int getPartitionIndex(int arr[], int low, int high) 
    { 
   	    int pivot_element = arr[high];
        
        int i = low - 1;
        int j;
        for (j=low; j<high; j++)
        {
            if (arr[j] < pivot_element)
            {
                i++;
                swap(arr, i, j);
            }
        } 
        i++;
        swap(arr, i, j);
        return i;
    } 
    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    void sort(int arr[], int low, int high) 
    {  
        if (low >= high)
        {
            return;
        }
        
            // Recursively sort elements before 
            // partition and after partition 
        int partition_index = getPartitionIndex(arr, low, high);
        sort(arr, low, partition_index - 1);
        sort(arr, partition_index + 1, high);
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
        int arr[] = {12,11,13,-5,6,7,-4,1,8,-9,2,1}; 
        int n = arr.length; 
  
        QuickSort ob = new QuickSort(); 
        ob.sort(arr, 0, n-1); 
  
        System.out.println("sorted array"); 
        printArray(arr); 
    } 
} 