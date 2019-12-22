// Time Complexity :
//    swap() - O(1)
//    partition() - O(n)
//    sort() - O(n^2)
//      
// Space Complexity :
//    swap() - O(1)
//    partition() - O(n)
//    sort() - O(1)
// Did this code successfully run on Leetcode : N/A
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
   	  //Write code here for Partition and Swap
      //choose pivot as the first element
      int X = arr[low];
      //choose a pointer i pointing to first element
      int i = low;

      //loop j from low to high
      for(int j=low+1; j <= high; ++j)
      {
        //if arr[j] is not in the right partition
        if(arr[j] < X)
        {
          ++i;
          //loop invariance swap
          swap(arr, i, j);
        }
      }
      //swap pivot to its righful place
      swap(arr, low, i);
      return i;
    }

    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    void sort(int arr[], int low, int high) 
    {  
      // Recursively sort elements before 
      // partition and after partition

      if(low < high)
      {
        int xPos = partition(arr, low, high);
        //Recursively sort the two partitions
        sort(arr, low, xPos-1);
        sort(arr, xPos+1, high);
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
