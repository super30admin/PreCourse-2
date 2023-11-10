// Time Complexity : O(N^2)
// Space Complexity : O(N)
// Did this code successfully run on Leetcode : ran it successfully on local machine
/* Any problem you faced while coding this : Had to read about the steps of the algo and also about recursion and 
also found it bit difficult to calculate the time and space complexity of any algo*/

/*
-- Choose the last element of the array as the pivot. Now start traversing the array from the start.
-- As soon as we encounter element which is greater than the pivot assign it as the leftpointer.
-- Then continue traversing the array till we get an element smaller than the pivot. Now swap this smaller element with the leftpointer.
-- Now increment the leftpointer by one and again continue traversing the array and repeat this swapping process whenever we encounter an element smaller than the pivot element.
-- Once we reach the second last element swap the pivot element with the leftpointer.
-- Repeat all the above steps for elements on the left and right of the leftpointer recursively and repeat this till we further cannot partition the array.
*/ 
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
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
    
    int partition(int arr[], int low, int high) 
    { 
   	//Write code here for Partition and Swap
        int leftPointer = low;
        for(int i=low;i<high;i++){
            if(arr[i]<=arr[high]){

                swap(arr,i,leftPointer);
                leftPointer++;
            }    
        }
        swap(arr, leftPointer, high);
        return leftPointer;

    } 
    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    void sort(int arr[], int low, int high) 
    {  
            // Recursively sort elements before 
            // partition and after partition
            if(low>=high){
                return;
            }
                int partIndex = partition(arr,low,high);
                sort(arr,partIndex+1,high);
                sort(arr,low,partIndex-1);
            
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
        int arr[] = { 6, 7, 2, 1, 5, 1, 4, 3 }; 
        int n = arr.length; 
  
        QuickSort ob = new QuickSort(); 
        ob.sort(arr, 0, n-1); 
  
        System.out.println("sorted array"); 
        printArray(arr); 
    } 
} 
