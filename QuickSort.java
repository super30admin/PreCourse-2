// Time Complexity :O(NlogN)
// Space Complexity : O(1) we are sorting inplace here
// Did this code successfully run on Leetcode :
// Any problem you faced while coding this :


// Your code here along with comments explaining your approach
// Taking the first element as the pivot and arranging the other
// elements w.r.t to that pivot and then recursively applying the quick sort to the two seperate portins of the array
import java.util.Arrays;

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
        //Your code here
    }

    int partition(int arr[], int low, int high)
    {
        int pivot = low;
        while(low < high){
            while(low < arr.length-1 && arr[low] <= arr[pivot] ){
                low++;
            }
            while(high > 0 && arr[high] > arr[pivot]){
                high--;
            }
            
            if (low<high){
                swap(arr,high,low);
                System.out.println("swap");
            }
        }
        swap(arr,high,pivot);
        
        
        return high;
        //Write code here for Partition and Swap
    }
    /* The main function that implements QuickSort()
      arr[] --> Array to be sorted,
      low  --> Starting index,
      high  --> Ending index */
    void sort(int arr[], int low, int high)
    {
        if(low<high){
            int p = partition(arr,low,high);
            sort(arr,low,p-1);
            sort(arr,p+1,high);

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
        int arr[] = {10};
        int n = arr.length;

        QuickSort ob = new QuickSort();
        ob.sort(arr, 0, n-1);

        System.out.println("sorted array");
        printArray(arr);
    }
}
