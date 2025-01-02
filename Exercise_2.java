// Time Complexity : O(nlogn)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : No


// Your code here along with comments explaining your approach
// I have taken the middle element as the pivot, and partitioned the array based on the pivot value
// Move all elements less than pivot to the left of the pivot and elements greater than pivot to the right half 
// and then recursively call the partition until the entire array is sorted



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
        int i=low, j= high;
        int pivot = arr[(low+high)/2];
        System.out.println("i "+i+" pivot "+pivot+" j "+j);
        while(i<=j){
            while(arr[i] < pivot){
                i++;
            }
            while(arr[j] > pivot){
                j--;
            }
            //System.out.println("i "+i+" pivot "+pivot+" j "+j);
            if(i<=j){
                swap(arr, i, j);
                i++;
                j--;
            }
           // System.out.println("swapped i "+i+" pivot "+pivot+" j "+j);
           // printArray(arr);
        }
        //System.out.println("end for loop i "+i+" pivot "+pivot+" j "+j);
        return i;
        //Write code here for Partition and Swap
    }
    /* The main function that implements QuickSort()
      arr[] --> Array to be sorted,
      low  --> Starting index,
      high  --> Ending index */
    void sort(int arr[], int low, int high)
    {
        int index = partition(arr, low,high);
        if(low < index-1) {
            sort(arr, low, index-1);
        }
        if(high > index) {
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
        int n = arr.length;

        QuickSort ob = new QuickSort();
        System.out.println("Before array");
        printArray(arr);
        ob.sort(arr, 0, n-1);

        System.out.println("sorted array");
        printArray(arr);
    }
} 
