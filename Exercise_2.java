// Time Complexity : O (n log n)
// Space Complexity : O (log n)
// Did this code successfully run on Leetcode : Ran it on VS Code. 
// Any problem you faced while coding this : No

// Your code here along with comments explaining your approach
// Check if low is less than high, then find the partition index for the given array and recursively call
// sort method on left and right part of partition. To find the partition index of a given array start with 
// last element as pivot. Take two pointers i and j that start from index 0 and check if value at index i in 
// array is less than or equal to pivot element, if we find such element swap elements at index i and j.
// Increment j value only on swap. Continue this until i reaches end of array. This gives the final index of
// pivot element in the sorted array. 

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
       int pivot = arr[high];
       int j = 0;
       for(int i=0;i<=high;i++){
           if(arr[i]<=pivot){
              swap(arr, i, j);
              j++;
           }
       }
       return --j;
    } 
    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    void sort(int arr[], int low, int high) 
    {  
            // Recursively sort elements before 
            // partition and after partition
            if(low<high){
                int index = partition(arr, low, high);
                sort(arr, low, index-1);
                sort(arr, index+1, high);
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
