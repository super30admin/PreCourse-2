// Time Complexity : O(nlogn)
// Space Complexity : O(logn)

import java.util.Stack;

class IterativeQuickSort {
    void swap(int arr[], int i, int j) {
        // Try swapping without extra variable
        if (i != j) {
            arr[i] = arr[i] + arr[j];
            arr[j] = arr[i] - arr[j];
            arr[i] = arr[i] - arr[j];
        }
    }

    /*
     * This function is same in both iterative and recursive
     */
    int partition(int arr[], int l, int h) {
        {
            // Assuming the pivot is the last element
            int i = l - 1;
            int pivot = arr[h];

            // If element at index j is less than pivot, swap i and j elements
            for (int j = l; j < h; j++) {
                if (arr[j] <= pivot) {
                    i++;
                    swap(arr, i, j);
                }
            }
            swap(arr, i + 1, h);
            return i + 1;
        }
    }

    // Sorts arr[l..h] using iterative QuickSort
    void QuickSort(int arr[], int l, int h) {

        // Try using Stack Data Structure to remove recursion.

        // initializing stack for storing the low and high indexes
        Stack<Integer> quickStack = new Stack<>();
        quickStack.push(l);
        quickStack.push(h);

        // running untill the stack is empty
        while (!quickStack.isEmpty()) {
            h = quickStack.pop();
            l = quickStack.pop();

            // calling partition to set the pivot at its correct position
            int part = partition(arr, l, h);

            // pushing the indexes of the left half of pivot
            if (part - 1 > l) {
                quickStack.push(l);
                quickStack.push(part - 1);
            }

            // pushing the indexes of the right half of pivot
            if (part + 1 < h) {
                quickStack.push(part + 1);
                quickStack.push(h);
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