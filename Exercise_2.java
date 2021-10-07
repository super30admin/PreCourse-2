// Time Complexity : O(nlog n) is best case and O(n2) is worst case
// Space Complexity : O(log n)
// Did this code successfully run on Leetcode : no
// Any problem you faced while coding this :
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
    
    int partition(int arr[], int low, int high) 
    { 
      int pindex = low;
      int pivot = high;
      for(int i = low; i < high; i++)
      {
        if(arr[i] <= pivot)
        {
          swap(arr, i, pindex);
          pindex = pindex + 1;
        }

      }
      swap(arr, pindex, high);
      return pindex;
    } 

    void sort(int arr[], int low, int high) 
    {  
      int pindex;
      if(low < high) {
        pindex = partition(arr, low, high);
        sort(arr, low, pindex - 1);
        sort(arr, pindex + 1, high);
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
