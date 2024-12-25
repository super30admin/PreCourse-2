// Time Complexity : Best Case:- O(nlogn),  Worst Case:- O(n²)
// Space Complexity : O(logn)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : No

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
        int temp = arr[j];
        arr[j] = arr[i];
        arr[i] = temp;
    }
    
    int partition(int arr[], int low, int high)
    { 
        int leftIndex = low;
        int rightIndex = high;
        while(leftIndex < rightIndex) {
            while(arr[leftIndex] <= arr[high] && leftIndex < rightIndex) {
                leftIndex++;
            }
            while(arr[rightIndex] >= arr[high] && rightIndex > leftIndex) {
                rightIndex--;
            }
            swap(arr, leftIndex, rightIndex);
        }
        swap(arr, leftIndex, high);
        return leftIndex;
    } 
    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    void sort(int arr[], int low, int high) 
    {  
        // Recursively sort elements before
        // partition and after partition
        if(low >= high) {
            return;
        }
        int leftIndex = partition(arr, low, high);
        sort(arr, low, leftIndex-1);
        sort(arr, leftIndex+1, high);
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
