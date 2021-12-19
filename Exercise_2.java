// Time Complexity : O(n2)
// Space Complexity : O(n)
// Did this code successfully run on Leetcode : Tested successfully on local code editor.
// Any problem you faced while coding this : No

//Approach: Quicksort is based on divide and conquer approach. The array is divided into subarrays based on a pivot element such that elements smaller than pivot
//are on the left of the pivot and element greater than pivot are on its right. This is done recursively for the left and right subarrays till a single element is
//left in the array. The resulting array is sorted.
// partition() method returns the pivot index. Inside the partition method, I have taken the rightmost element as the pivot and rearranged the array as mentioned above

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
        int p = low-1;
        int i = low;
        int pivot = arr[high];
        while(i < high) {
            if(arr[i] <= pivot) {
                p++;
                swap(arr, i, p);
            }
            i++;
        }
        swap(arr, high, p+1);
        return p+1;
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
            int pivot = partition(arr, low, high);
            sort(arr, low, pivot-1);
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
        int arr[] = {10, 7, 8, 9, 1, 5};
        int n = arr.length;

        QuickSort ob = new QuickSort();
        ob.sort(arr, 0, n-1);

        System.out.println("sorted array");
        printArray(arr);
    }
}