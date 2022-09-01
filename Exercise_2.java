// Time Complexity :  Best case : O(NlogN), worst case: O(N^2)
// Space Complexity : Best Case: O(logN), worst case: O(N)
// Did this code successfully run on Leetcode : Not for the input [5,1,1,2,0,0] on leetcode but it works here succesfully
// Any problem you faced while coding this : First time learning the algorithm.
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
        int temp;
        // This is the real meat for recursive logic
        if(i >=0 && j >= 0) {
            temp = arr[j];
            arr[j] = arr[i];
            arr[i] = temp;
        } else {
            System.out.println(i + " or " + j + " are out of bounds");
        }
    }

    int partition(int arr[], int low, int high)
    {
   	//Write code here for Partition and Swap
        int pivot = arr[(low + high)/2];

        while (low <= high) {
            while (arr[low] < pivot) low ++;
            while (arr[high] > pivot) high--;

            // Swap elements after we fing high el < pivot and low el > pivot
            if (low <= high) {
                swap(arr, low, high);
                low++;
                high--;
            }
        }
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
        int index = partition(arr, low, high);
        if (low < index - 1) {
            sort(arr, low, index - 1);
        }
        if (index < high) {
            sort(arr, index, high);
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
//        int arr[] = {5,1,1,2,0,0};
        int n = arr.length;

        QuickSort ob = new QuickSort();
        ob.sort(arr, 0, n-1);

        System.out.println("sorted array");
        printArray(arr);
    }
}
