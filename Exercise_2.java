/*
    1. Time Complexity : O(nlogn)   Worst Case : O(n2)
    2. Space Complexity : O(logn)   Worst Case : O(n)   
    3. Did this code successfully run on Leetcode :
    4. Any problem you faced while coding this : -
 */

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

    int partition(int arr[], int low, int high) {
        int pivot = high;
        int i = low - 1, j = low;
        while (j < high) {
            if (arr[j] < arr[pivot]) {
                swap(arr, ++i, j);
            }
            ++j;
        }
        swap(arr, i+1, pivot);
        return i+1;

    } 
    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    void sort(int arr[], int low, int high) 
    {  
        if (low >= high) return;
        int pivot = partition(arr, low, high);
        sort(arr, low, pivot - 1);
        sort(arr, pivot + 1, high);
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
