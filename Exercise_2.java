// Time Complexity :
/*
Best/Average : O(n * Log n)
Worst : O(n^2) // If array is sorted in decreasing order and pivot will be left most/ right most while partitioning
*/

// Space Complexity : O(N)


// Did this code successfully run on Leetcode : n/a
// Any problem you faced while coding this : No


// Your code here along with comments explaining your approach
/*
Initially pivot element is last element in the array then after partitioning 
we get index of partition such that it's left side contains elements less than element at partition index and 
right side have greater than element at partition index
*/

// Call sort() function recursively for indices left to part-1 and part+1 to high


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
        arr[i] =  arr[j];
        arr[j] = temp;
    }
    
    int partition(int arr[], int low, int high) 
    { 
   	//Write code here for Partition and Swap 
        int pivot = arr[high];
        int c = low - 1;

        for(int i = low; i < high; i++){
            if(arr[i] <= pivot){
                c++;
                swap(arr, c, i);
            }
        }
        swap(arr, c+1, high);
        return c+1;
    } 
    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    void sort(int arr[], int low, int high) 
    {  
            // Recursively sort elements before 
            // partition and after partition 
            if(low <= high){
                int part = partition(arr, low, high);
                //System.out.println("Partition : " + part);
                
                sort(arr, low, part - 1);
                sort(arr, part + 1, high);
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
