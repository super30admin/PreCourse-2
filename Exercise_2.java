// Time Complexity : O(nlogn) worst case O(n^2)
// Space Complexity : O(log n)
// Did this code successfully run on Leetcode : n/a
// Any problem you faced while coding this : yes, few problems, regarding the algorithm but I found the detailed explanation in youtube, so I was able to code it out at last.


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
        int mid = (low+high)/2;
        int pivot = arr[mid];
        //extreme left pointer
        int i = low;
        //extreme right pointer
        int j = high;
        //placing the pivot element at last(high)
        swap(arr, mid, high);
        //rearranging the elements wrt pivot
        while(i<j)
        {
            //move the left pointer till it encounters the element greater than or equal to the pivot and the stop for swapping
            while(i<=high && arr[i]<pivot)
                i++;
            //move the right pointer till it encounters the element lesser than the pivot and stop for swapping with left pointer.
            while(j>=0 && arr[j]>=pivot)
                j--;
            //there is a chance of crossing eachother that means elements are in correct order no need to swap, if they don't cross eachother that means we  need to swap.
            if(i<j)
                swap(arr, i, j);
        }
        //finally we put the pivot at its right position, since we swapped it with arr[high] and the i will be pointing to the element greater than pivot, we just swap them.
        swap(arr, high, i);
        //return the partition index;
        return i;
    } 
    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    void sort(int arr[], int low, int high) 
    {  
        if(low<high)
        {
            //get the partition index from the partition method which fixes the position of one element.
            int mid = partition(arr, low, high);
            //now recursively perform the same sorting to the left half.
            sort(arr, low, mid-1);
            //recursively perform the same sorting to the right half as well.
            sort(arr, mid+1, high);
        }
            // Recursively sort elements before 
            // partition and after partition 
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
