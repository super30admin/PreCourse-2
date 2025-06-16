// Time Complexity : Avg: O(n log n), Worst: O(n^2) [When we pick the smallest or largest element as the pivot]
// Space Complexity : Avg: O(log n) stack space, Worst: O(n) [When the pivot is the smallest or largest element]
// Did this code successfully run on Leetcode : yes
// Any problem you faced while coding this : no
/*
Approach:

1. QuickSort is a sorting algorithm that picks an element as the pivot.
   It rearranges the array so that elements smaller than the pivot are on the left,
   and elements greater than the pivot are on the right.

2. In the sort function:
   We call the partition function to find the correct position of the pivot.
   Then we recursively sort the subarrays to the left and right of the pivot.

3. In the partition function:
   We take arr[high] as the pivot.
   We use a variable i to track the last index where a smaller element is placed.
   As we loop from l to h - 1, if arr[j] < pivot, we increment i and swap arr[i] and arr[j].
  After the loop, we place the pivot in its correct sorted position by swapping arr[i + 1] and arr[high].

4. In the swap function:
   We simply exchange the elements at the two given indices.
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
        int i = low-1;
        
        for(int j = low; j < high; j++){
            if(arr[j] < pivot){
                i++;
                swap(arr, i, j);
            }
        }
        swap(arr, i + 1, high); 
        return i + 1;
    } 
    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    void sort(int arr[], int low, int high) 
    {  
            // Recursively sort elements before 
            // partition and after partition 
            if (low < high) {

                int pi = partition(arr, low, high); 
    
                sort(arr, low, pi - 1);  
                sort(arr, pi + 1, high); 
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
