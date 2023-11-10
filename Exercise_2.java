// Time Complexity : 
/*
Best Case - O(nLogn)
    (Partition is always in the middle) 
    There are Logn levels and in each level partition algorithm will compare the elements for     n times. Hence, O(nLogn) 
Worst Case - O(n^2)
    (Partition always picks greatest or smallest element as pivot. This happens when the array     is already sorted in ascending or descending order) 
    First partitioning element makes 'n' comparisons, 
    Next partitioning element makes 'n-1' comparisons,
    Next partitioning element makes 'n-2' comparisons,
    The comparisons will end as --- ...,2,1 
    The above is equal to n(n+1)/2 
    Hence, O(n^2)
Average Case - Mathematically it is found to be O(nLogn)
*/
// Space Complexity :
/* 
    Best case - O(Logn)
    Worst case - O(n)
*/
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : N/A

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
   	//Code for Partition and Swap 
        int i = low-1;
        int pivot = arr[high];
        
        for(int j = low; j<=high-1; j++)
        {
            if(arr[j] < pivot)
            {
                i++;
                swap(arr,i,j);
            }
        }
        swap(arr, i+1, high);
        return i+1;
        
    } 
    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    void sort(int arr[], int low, int high) 
    {  
        // Recursively sort elements before 
        // partition and after partition
        if(low<high)
        {
            int pi = partition(arr,low,high);
            sort(arr,low,pi-1);
            sort(arr,pi+1,high);
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