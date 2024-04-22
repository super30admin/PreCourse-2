// Time Complexity : O(n log n) where n is the number of elements in the array
// Space Complexity : O(1) as we are not using any extra space
// Did this code successfully run on Leetcode : NA
// Any problem you faced while coding this : No

// Your code here along with comments explaining your approach : The swap method swaps two elements in an array. The partition method chooses the last element as the pivot, places the pivot element at its correct position in the sorted array, and places all smaller elements to the left of the pivot and all greater elements to the right of the pivot. The QuickSort method sorts the array using the iterative approach. The printArr method is a utility function to print the array. The main method creates an array and sorts it using the quick sort algorithm.

class IterativeQuickSort {
    void swap(int arr[], int i, int j) {
        if (i != j) {
            arr[i] = arr[i] + arr[j];
            arr[j] = arr[i] - arr[j];
            arr[i] = arr[i] - arr[j];
        }
    }

    /*
     * This function is same in both iterative and
     * recursive
     */
    int partition(int arr[], int l, int h) {
        int pivot = arr[h];
        int i = (l - 1);
        for (int j = l; j < h; j++) {
            if (arr[j] < pivot) {
                i++;
                swap(arr, i, j);
            }
        }
        swap(arr, i + 1, h);
        return i + 1;
    }

    // Sorts arr[l..h] using iterative QuickSort
    void QuickSort(int arr[], int l, int h) {
        Stack<Integer> stack = new Stack<>();
        stack.push(l);
        stack.push(h);

        while (!stack.isEmpty()) {
            h = stack.pop();
            l = stack.pop();

            int p = partition(arr, l, h);

            if (p - 1 > l) {
                stack.push(l);
                stack.push(p - 1);
            }

            if (p + 1 < h) {
                stack.push(p + 1);
                stack.push(h);
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