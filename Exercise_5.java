// Time Complexity : Time complexity of quicksort is O(nLog(n)) for best case and average case 
//and O(n^2) for worst case
// Space Complexity : There is extra space required due to stack so space complexity is O(n)
// Did this code successfully run on Leetcode : could not find it on leetcode
// Any problem you faced while coding this :
// Had to debug a lot to find problems in the algorithm
// Had to look up time and space complexity for quicksort
// Had to lookup iterative quicksort as I could not recollect how to code that

// Your code here along with comments explaining your approach

import java.util.Stack;

class IterativeQuickSort {
    void swap(int arr[], int i, int j) {
        // Try swapping without extra variable
        if (i != j) {
            arr[i] = arr[i] + arr[j];
            arr[j] = arr[i] - arr[j];
            arr[i] = arr[i] - arr[j];
        }

        // int temp = arr[i];
        // arr[i] = arr[j];
        // arr[j] = temp;
    }

    /*
     * This function is same in both iterative and
     * recursive
     */
    int partition(int arr[], int low, int high) {
        // Compare elements and swap.
        // Write code here for Partition and Swap
        // Variable pivot which is the last element in the array. Pivot will be used to
        // compare and divide the array in 2 parts
        int pivot = high;
        high--; // As pivot is the highest element, making the highest element as the one before
                // pivot
        // Lopp will run while the low and high pointer do not cross
        while (low <= high) {
            while (low <= high && arr[low] <= arr[pivot]) { // To find the element on the left side of the array to swap
                low++;
            }
            while (low <= high && arr[high] >= arr[pivot]) { // To find the element on the right side of the array to
                                                             // swap
                high--;
            }
            if (low <= high)
                swap(arr, high, low); // Swap the elements on left and right side
        }

        swap(arr, low, pivot); // Swap the elements to get the pivot element right in between the two parts of
                               // array
        return low;
    }

    // Sorts arr[l..h] using iterative QuickSort
    void QuickSort(int arr[], int l, int h) {
        // Try using Stack Data Structure to remove recursion.
        // Using stack for iterative quicksort
        Stack<Integer> stk = new Stack<>();

        // Push low and high variable into stack
        stk.push(l);
        stk.push(h);
        // Lopp will run till the stack is empty
        while (!stk.isEmpty()) {
            // Get the topmost low and high to use for partition
            int high = stk.pop();
            int low = stk.pop();
            int p = partition(arr, low, high);

            // Put low and high in stack if left side is present after partition
            if (p - 1 > low) {
                stk.push(low);
                stk.push(p - 1);
            }
            // Put low and high in stack if right side is present after partition
            if (p + 1 < high) {
                stk.push(p + 1);
                stk.push(high);
            }
        }

    }

    // A utility function to print contents of arr
    void printArr(int arr[], int n) {
        int i;
        for (i = 0; i < n; ++i)
            System.out.print(arr[i] + " ");
    }

    // Driver code to test above
    public static void main(String args[]) {
        IterativeQuickSort ob = new IterativeQuickSort();
        int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 };
        ob.QuickSort(arr, 0, arr.length - 1);
        ob.printArr(arr, arr.length);
    }
}