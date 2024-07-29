
// Time Complexity : O(nlog(n))
// Space Complexity : O(log(n))// recursion
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : Initially faced issue with how to get the pivot element.
// But all good.



// Identify the pivot element
// each pass will fix the position of the pivot element, so that the left side of the pivot element is less than the pivot element and the right side is greater than the pivot element.
// Pivot element can be found out by initially fixing the pivot position and the value and then comparing.


// Java implementation of QuickSort

class QuickSort {

    // A utility function to swap two elements
    static void swap(int[] arr, int i, int j)
    {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    static int partition(int[] arr, int low, int high)
    {
        int pivot= arr[high];// pivot element.
        int j = low; 
        while(low< high) {
            // swap the element which is less than the pivot with the element which is greater than the pivot.
            if(arr[low]<= pivot) {
                swap(arr, low, j);// you are taking the larger than pivot element and swapping with the lower than pivot element.
                j++; // increase the pivot index.
                // the movement is such that the greater than pivot element will be filtered to the right side.
            }
            low++;
        }
        swap(arr,j, high);// then swap the pivot(essentially the middle element) with the greater than the pivot element.
        return j;
    }

    static void quickSort(int[] arr, int low, int high)
    {
        if(low>= high) {
            return;
        }

        if (low < high) {// why low < high, we are also checking for 2 elements. It will only stop at 
            // when there is only 1 element.

            // is now at right place
            int pivot = partition(arr, low, high);
            // pivot index 
            quickSort(arr, low, pivot - 1);
            quickSort(arr, pivot + 1, high);
        }
    }
    // To print sorted array
    public static void printArr(int[] arr)
    {
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
    }

    // Driver Code
    public static void main(String[] args)
    {
        int[] arr = { 10, 7, 8, 9, 1, 5 };
        int N = arr.length;

        // Function call
        quickSort(arr, 0, N - 1);
        System.out.println("Sorted array:");
        printArr(arr);
    }
}
