/*
 Time complexity: O(NlogN) average and best case and O(N2) in worst case. It will depend on the selection of pivot.
 Scpace complexity: worst case O(N) and average case (logN) since we will roughly partition the array space into two parts
                    where N is size of Array
 Did this code successfully run on Leetcode : 
 Any problem you faced while coding this : Yes, i had to go back and understand quick sort algothim and implement the code
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
        //Your code here
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
    
    int partition(int arr[], int low, int high) 
    { 
        //Write code here for Partition and Swap 
        int pivot = arr[high];
        int i = low, j = high;
        
        //after the loop breaks we have array arranged in such a way that all elements on left side is less than pivot 
        //and all elements which is greater than pivot is on right side.
        while(i < j){
            
            //till we find an element which is greater that pivot
            while(i < j && i <= high && arr[i] <= pivot){
                i++;
            }
            
            //till we find an element which is lesser than pivot
            while(i < j && j>=0 && arr[j] >= pivot){
                j--;
            }

            //swap to make larger element go to left side and smaller element go to right side
            if(i < j){
                swap(arr, i, j);
            }
        }
        //we found correct position of pivot element
        if(i <= high){
            swap(arr, high, i);
        }
        return i; // return position if the element which is at its correct position
    } 
    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    void sort(int arr[], int low, int high) 
    {  
            // Recursively sort elements before 
            // partition and after partition
            //make sure we have atlease two elements in the array space
            if(low < high){
                int pivot = partition(arr, low, high);
                sort(arr, low, pivot-1);
                sort(arr, pivot + 1, high);
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
        
        System.out.println("before sort"); 
        printArray(arr); 
        QuickSort ob = new QuickSort(); 
        ob.sort(arr, 0, n-1); 
  
        System.out.println("sorted array"); 
        printArray(arr); 
    } 
} 
