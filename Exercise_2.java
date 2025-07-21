// Time Complexity : O(n logn) - average case and O(n^2) - worst case
// Space Complexity : O(n) due to recursion stack length
// Did this code successfully run on Leetcode : Yes, but TLE error for larger input
// Any problem you faced while coding this : I forgot the quick sort algo, so had to revise it before implementing
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
        int tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
    }

    int partition(int arr[], int low, int high)
    {
        //Write code here for Partition and Swap
        int pivot = arr[high];
        // i tracks the index to place the elements lower than pivot from left to right
        int i = low - 1;

        for(int j= low; j<= high-1; j++) {
            if(arr[j] < pivot){
                i++;
                swap(arr, i, j);
            }
        }

        // i+1 is the index of pivot element
        swap(arr,i+1, high);
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
        if(low < high) {
            int pivotIdx = partition(arr, low, high);
            sort(arr, low, pivotIdx-1);
            sort(arr, pivotIdx+1, high);
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
