// Time Complexity : O(n logn) - average case and O(n^2) - worst case
// Space Complexity : O(n) - stack size
// Did this code successfully run on Leetcode : Yes but TLE error for larger input
// Any problem you faced while coding this : There was a bug in the swap function, fixed it by debugging
import java.util.ArrayDeque;
import java.util.Deque;

class IterativeQuickSort {
    void swap(int arr[], int i, int j)
    {
        //Try swapping without extra variable
        if(i == j) {
            return;
        }
        arr[i] = arr[i] + arr[j];
        arr[j] = arr[i] - arr[j];
        arr[i] = arr[i] - arr[j];
    }

    /* This function is same in both iterative and
       recursive*/
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

    // Sorts arr[l..h] using iterative QuickSort
    void QuickSort(int arr[], int l, int h)
    {
        //Try using Stack Data Structure to remove recursion.
        Deque<Integer> stack = new ArrayDeque<>();

        stack.push(h);
        stack.push(l);

        while(!stack.isEmpty()) {
            int low = stack.pop();
            int high = stack.pop();

            int pivotIdx = partition(arr, low, high);

            if(pivotIdx +1 < high) {
                stack.push(high);
                stack.push(pivotIdx +1);
            }

            if(pivotIdx -1 > low){
                stack.push(pivotIdx -1);
                stack.push(low);
            }
        }
    }

    // A utility function to print contents of arr
    void printArr(int arr[], int n)
    {
        int i;
        System.out.println("\nArray:");
        for (i = 0; i < n; ++i)
            System.out.print(arr[i] + " ");
    }

    // Driver code to test above
    public static void main(String args[])
    {
        IterativeQuickSort ob = new IterativeQuickSort();
        int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 };
        ob.QuickSort(arr, 0, arr.length - 1);
        ob.printArr(arr, arr.length);
    }
} 