// Time Complexity : O(Nlogn)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : Not applicable
// Any problem you faced while coding this : calculating time complexity    

// Approach : get the pivot element sorted out such that the elements towards the left of the pivot are less than pivot
// and the elements that are greater than pivot are towards the right of pivot 
// and recursively call the quicksort function on left and right sub arrays.

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
        int temp=arr[i];
        arr[i]=arr[j];
        arr[j]=temp; 
    }
    
    int partition(int arr[], int low, int high) {
        
        int pivot = arr[high];
        int i = (low - 1);
        for (int j = low; j < high; j++) {
            if (arr[j] <= pivot) {
                i++;
                // System.out.println("i and j before swap"+ i + j ); 
                swap(arr, i, j);
                // System.out.println("After swap" ); 
                // printArray(arr); 
            }
        }

        swap(arr, i + 1, high);
        return (i + 1);
    }
    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    void sort(int arr[], int low, int high) 
    {  
        // System.out.println("Original");
        // printArray(arr);
            // Recursively sort elements before 
            // partition and after partition 
        if(low<high){
            int pivot=partition(arr,low,high);

            sort(arr,low,pivot-1);
            sort(arr,pivot+1,high);
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
