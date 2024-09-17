// Time Complexity : O(n^2)
// Space Complexity : O(1) as no extra space is used.
// Did this code successfully run on Leetcode : No couldn't find in LeetCode, but executed successfully in IDE
// Any problem you faced while coding this : No
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
        int temp;
        temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    int partition(int arr[], int low, int high)
    {
        //Write code here for Partition and Swap
        int pivot = arr[high];
        int ptr1 = low-1;
        for(int ptr2=low; ptr2<high; ptr2++){
            if(arr[ptr2] <= pivot){
                ptr1++;
                swap(arr,ptr1,ptr2);
            }
        }
        swap(arr,ptr1+1,high);
        return ptr1+1;
    }
    /* The main function that implements QuickSort()
      arr[] --> Array to be sorted,
      low  --> Starting index,
      high  --> Ending index */
    void sort(int arr[], int low, int high)
    {
        // Recursively sort elements before
        // partition and after partition
        if(low < high){
            int piv = partition(arr,low,high);
            sort(arr,low,piv-1);
            sort(arr,piv+1,high);
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

