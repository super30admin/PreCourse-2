// Time Complexity : O(NlogN) 
// Space Complexity : O(1) 
// Did this code successfully run on Leetcode : Yes 
// Any problem you faced while coding this:  No
// Your code here along with comments explaining your approach: We consider the first element of the array as pivot, the first index as low, and the last as high. Then we increment low until an element greater than pivot is found and we decrement high until an element lesser than pivot is found. Once that is done, we swap those elements. We keep doing this until the low becomes greater than the high. We keep all the elements lesser than the pivot, to its left side, and all the elements greater than it to its right. Hence we have two function calls for sort. The index where the pivot is placed becomes the partition.

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
    
    int partition(int arr[], int low, int high) 
    { 
   	//Write code here for Partition and Swap 
        int i=low, j=high, pivot=arr[low];

        while(i<j)
        {
            while(arr[i]<=pivot && i<=high-1)
            {
                i++;
            }
            while(arr[j]>pivot && j>=low+1)
            {
                j--;
            }

            if(i<j)
            {
                swap(arr,i,j);
            }
        }
        swap(arr,low,j);
            return j;

    } 
    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */


    void sort(int arr[], int low, int high) 
    {  
            // Recursively sort elements before 
            // partition and after partition 
            if (low<high)
            {
                int pindex=partition(arr, low, high);
                sort(arr,low,pindex-1);
                sort(arr,pindex+1,high);
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
