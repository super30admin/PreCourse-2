/*
Time complexity:
Space Complexity:
Did this code successfully run on Leetcode:
Any problem you faced while coding this: 

Code along with comments explaining my approach is as follows
*/

class IterativeQuickSort {
    void swap(int arr[], int i, int j) {
        // Try swapping without extra variable
        int tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
    }

    /*
     * This function is same in both iterative and
     * recursive
     */
    int partition(int arr[], int l, int h) {
        // Compare elements and swap.
        int v = arr[h];
        int i = (l - 1);
        for (int j = l; j <= h - 1; j++) {

            if (arr[j] <= v) {
                i++;
                swap(arr, i, j);
            }
        }
        swap(arr, i + 1, h);
        return i + 1;

    }

    // Sorts arr[l..h] using iterative QuickSort
    void QuickSort(int arr[], int l, int h) {
        // Try using Stack Data Structure to remove recursion.

        int[] stack = new int[h - l + 1];

        int top = -1;

        // pushing initial values of l and h to stack
        stack[++top] = l;
        stack[++top] = h;

        while (top >= 0) {// Until stack is empty

            h = stack[top--];
            l = stack[top--];

            int j = partition(arr, l, h);

            // Push elements on left side of pivot onto the stack

            if (j - 1 > l) {
                stack[++top] = l;
                stack[++top] = j - 1;

            }

            // Push elements on right side of pivot onto the stack
            if (j + 1 < h) {
                stack[++top] = j + 1;
                stack[++top] = h;

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