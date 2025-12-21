// Time Complexity : Average case - O(n logn), Worst Case - O(n^2) - based on what we choose as pivot
// Space Complexity : In place swapping, 0(1)
// Did this code successfully run on Leetcode :
// Ran into time limit exceeded error
// Any problem you faced while coding this : No
class QuickSort
{
    /* A utility function to swap elements at i and j index */
    void swap(int arr[],int i,int j){
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    /* This function takes last element as pivot,
       places the pivot element at its correct
       position in sorted array, and places all
       smaller (smaller than pivot) to left of
       pivot and all greater elements to right
       of pivot */
    int partition(int arr[], int low, int high) 
    {
        // select last element in the array for comparison
        int lastIndex = high;
        while (low < high) {
            // find first larger value(than the last value) from left
            while(low < high && arr[low] <= arr[lastIndex]){
                low++;
            }
            // find first smaller value(than the last value) from right
            while(low < high && arr[high] >= arr[lastIndex]){
                high--;
            }
            if(low >= high) break;
            // swap the larger and smaller value, so that all smaller values
            // are on left and larger values are on right
            swap(arr, low, high);
        }

        return low;
    } 
    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index
      Find the pivot, swap the pivot value with last element, so that array is divided into 2 halves,
      sort the left side of the pivot and the right side of the pivot*/
    void sort(int arr[], int low, int high) 
    {
        if(low >= high) return;

        int pivotIndex = partition(arr, low, high);
        swap(arr, pivotIndex, high);
        sort(arr, low, pivotIndex-1);
        sort(arr, pivotIndex+1, high);
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
