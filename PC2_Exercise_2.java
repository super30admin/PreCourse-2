// Time Complexity : nlog(n)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : No
// Any problem you faced while coding this : java.lang.ArrayIndexOutOfBoundsException: Index 6 out of bounds for length 6


// Your code here along with comments explaining your approach


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
        //swapped two elements using temp variable
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
    
    int partition(int arr[], int low, int high) 
    { 
   	//Write code here for Partition and Swap 
       int pivot = arr[low]; //declared a pivot to create partition of array
       int start = low ; //declared a start variable from lower bound of the array 
       int end = high  ; //declared an end variable from upper bound of the array 
       
        while(start < end){ //while loop  runs only when start < end 
            
            while(arr[start]<= pivot){
                start ++;
            }
            while(arr[end] >pivot){
                end--;
            }
            if(start < end){
                swap(arr, arr[start], arr[end]);
            }
        }
        swap(arr, arr[low],arr[end]); //if while loop cond not satisfied,simply swap will happen between low and end elements and end element will be returned
        return end;
    } 
    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    void sort(int arr[], int low, int high) 
    {  
            // Recursively sort elements before 
            // partition and after partition 
        if (low<high){
         //declared a local var loc which will store the value returned by partition    
        int loc = partition(arr, low,  high);
        
            //called sort() recursively on low,low-1,low+1,high bounds
        sort(arr, low, loc-1);
        sort(arr, loc+1, high);
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