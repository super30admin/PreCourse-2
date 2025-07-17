// Time Complexity : O(n^2) - depends on the input
// Space Complexity : O(n) stack memory
// Did this code successfully run on Leetcode : Timit limit exceeds as the leetcode problem looking for o(nlogn)
// Any problem you faced while coding this : Had to refresh my memory with the sorting technique. So took some help looking at the algorithm
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

    int partition(int arr[], int low, int high){
   	//Write code here for Partition and Swap
        // Setup the lowest element as the left pointer
        int leftPointer = low;

        // Iterate through the elements and swap the element with left pointer if at the current number is lesser than the pivot - high number in this case
        for(int i=low; i<high; i++) {
            if(arr[high]<arr[i]) {
                continue;
            }
            swap(arr, leftPointer, i);
            // Increment the left pointer for further swaps
            leftPointer++;
        }
        // swap the pivot element - (high in this case) with the leftPointer
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
        if(low<high) {
            // make two partitions with making sure the pivot element is picked and placed at its position in the array
            int pivot = partition(arr, low, high);
            // perform same steps for left sub array
            sort(arr, low, pivot-1);
            // perform same steps for right sub array
            sort(arr, pivot+1, high);
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
        int arr[] = {-10, 10, 7, 8, 2, 9, 1, 5};
        int n = arr.length;

        QuickSort ob = new QuickSort();
        ob.sort(arr, 0, n-1);

        System.out.println("sorted array");
        printArray(arr);
    }
}
