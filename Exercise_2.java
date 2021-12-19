// Time Complexity : best O(NlogN), worst O(n^2) where array is in desc order
// Space Complexity : O(1) as we only swap the positions
// Did this code successfully run on Leetcode : Ran it locally on IDE and works
                            //with multiple test cases
// Any problem you faced while coding this : No

class QuickSort
{
    /* This function takes last element as pivot,
       places the pivot element at its correct
       position in sorted array, and places all
       smaller (smaller than pivot) to left of
       pivot and all greater elements to right
       of pivot */
    void swap(int arr[],int i,int j)
    {
        //Your code here
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    int partition(int arr[], int low, int high)
    {
      //Write code here for Partition and Swap
      /*
        To partition, I adopted the methodology where in we find the actual
        position for pivot such that all elements to the left irrespective of
        their order for now are smaller than pivot and to the right are larger
      */
      int pivot = high;

      high = low;

      while(high < pivot)
      {
        if(arr[high] <= arr[pivot])
        {
          this.swap(arr, low, high);
          low++;
        }

        high++;
      }

      this.swap(arr, low, high);

      return low;

    }
    /* The main function that implements QuickSort()
      arr[] --> Array to be sorted,
      low  --> Starting index,
      high  --> Ending index */
    void sort(int arr[], int low, int high)
    {
      // Recursively sort elements before
      // partition and after partition
      //if during sorting index goes out of order so just return
      if(low >= high) return low;

      int partitionIndex = this.partition(arr, low, high);

      this.sort(arr, low, partitionIndex - 1);
      this.sort(arr, partitionIndex + 1, high);

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
