/**
 * Time Complexity = O(N^2) in worst case
 * Space Complexity = O(1) since everything has been done in place
 *
 * Leetcode:unable to find exact question number on leetcode
 *
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
        arr[i] = arr[j];
        arr[j] = temp;
    }

    int partition(int arr[], int low, int high)
    {
   	    //Write code here for Partition and Swap
        int pivot = arr[high];

        int left = low;
        int right = high -1;
//
//        arr[high] = pivot;

        while(left <= right) {

            if(arr[left] >pivot && arr[right] < pivot) {
                // swap the the left and right elements
                swap(arr, left, right);
                left++;
                right--;
            } else if(arr[left] > pivot) {
                // this mean we are good from the left index point of view
                right--;
            } else {
                // this mean we are good from right index point of view
                left++;
            }
        }

        int pivotIndex = left;
        swap(arr, pivotIndex, high);

        System.out.println("Patitioning at index "+ pivotIndex);

        return pivotIndex;
    }
    /* The main function that implements QuickSort()
      arr[] --> Array to be sorted,
      low  --> Starting index,
      high  --> Ending index */
    void sort(int arr[], int low, int high)
    {
            // Recursively sort elements before
            // partition and after partition

        if(low > high)
            return;

        int pivotIndex = partition(arr, low, high);
        sort(arr, low, pivotIndex -1);
        sort(arr, pivotIndex + 1, high);
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
        int arr[][] = {{10, 9, 8, 7, 6, 5}, {10, 7, 8, 9, 1, 5}};
        // ;
        int n = arr[0].length;

        QuickSort ob = new QuickSort();
        ob.sort(arr[0], 0, n-1);

        System.out.println("sorted array 1");
        printArray(arr[0]);

        ob.sort(arr[1], 0, n-1);
        System.out.println("sorted array 2");
        printArray(arr[1]);


    }
}
