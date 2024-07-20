// Time Complexity : O(nlogn)
// Space Complexity : 0(logn)
// Did this code successfully run on Leetcode : Local Environment (IntelliJ)
// Any problem you faced while coding this : No

class QuickSort
{
    void swap(int arr[],int i,int j){
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
    
    int partition(int arr[], int low, int high) 
    { 
   	    int pivot = arr[high];
        int small = low-1;
        for(int i=low; i<high; i++){
            if(arr[i] < pivot){
                small++;
                swap(arr, small, i);
            }
        }
        swap(arr, small+1, high);
        return small+1;
    } 

    void sort(int arr[], int low, int high) 
    {  
            int index = partition(arr, low, high);
            sort(arr, low, index-1);
            sort(arr, index+1, high);
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
