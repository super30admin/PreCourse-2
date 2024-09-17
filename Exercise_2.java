// Time Complexity : O(n^2) (where n is the number of elements in the array)
// Space Complexity : O(n) (array size)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : Yes, in partition method


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
        int temp = arr[i]; // use temp variable to store arr[i] 
        arr[i] = arr[j]; // copy arr[j] to arr[i]
        arr[j] = temp; // copy arr[i](temp) to arr[j]

    }
    
    int partition(int arr[], int low, int high) 
    { 
   	//Write code here for Partition and Swap 
        int pivot = arr[high]; // pivot element is last element
   	    int i = (low-1); // i = -1
   	    for (int j = low; j < high; j++) { // check if elemnt is less than pivot if yes, swap with i
   	        if (arr[j] < pivot) {
   	            i++;
   	            swap(arr, i, j);
   	        }
   	    }
   	    swap (arr, i+1, high); // swap pivot element when j and i cross each other. Get correct position of pivot element
   	    return i+1; // return the pivot position (partition)

    } 
    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    void sort(int arr[], int low, int high) 
    {  
            // Recursively sort elements before 
            // partition and after partition 
        if(low<high) {
        int part = partition(arr, low , high); // to get the correct position of pivot element to find the partition
        sort (arr,low, part-1); // sort left of partition
        sort (arr, part+1, high); // sort right of partition

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
