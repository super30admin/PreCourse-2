//Exercise_2 : Quick sort
// Time Complexity : Average Case : O(Nlog(N)), Worst Case: O(N^2)->When array is sorted in ascending or descending order
// Space Complexity : O(1) constant space because quick sort does sorting in place
// Did this code successfully run on Leetcode : No
// Any problem you faced while coding this :  No

/**** Steps ****/
/*
1) Find the partition  ---> Purpose to choose a pivot and move all elements smaller than pivot to the left and all the elements greater than pivot to the right, so that array array could be partitioned
       a) Pick last element which is high as pivot and partition index as low.
       b) Then traverse over the array starting from low to high-1 and compare all other elements with the pivot
       c) If any element is less than the pivot then swap that element with the element at partition index and increment the partition index
       d) Once traversal is completed swap the element at partition index with the chosen pivot;
       e) Return the partition index, from here problem will be segregated into sub problems. Because now part before the partition index and after the partition index is to be sorted.

2) Sort
    a) Make recursive call of below function until low index is less than the high index
           I) First find the partition index
           II) Make recursive call for the left partition which is from low index to the partition index - 1;
           III) Make recursive call for the right partition which is from partition index + 1 to high;      
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
        arr[i]   = arr[j];
        arr[j]   = temp;
    }
    
    int partition(int arr[], int low, int high) 
    { 
       //Write code here for Partition and Swap 
       
       int partIdx = low;
       int pivotIdx  = high;

       for(int i=low;i<=high-1;i++){
          
          if(arr[i]<arr[pivotIdx]){
              swap(arr,i,partIdx);
              partIdx++;
          }

       }

       swap(arr,partIdx,pivotIdx);
       
       return partIdx;

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
            int partIdx = partition(arr, low, high);

            sort(arr, low, partIdx-1);
            sort(arr, partIdx+1,high);
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
