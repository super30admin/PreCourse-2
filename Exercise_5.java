import java.util.Stack;

/*
Exercise_5 : Iterative Quick Sort.
// Time Complexity: O(N log N)
// Space Complexity: O(log N)
 */
class IterativeQuickSort {
    void swap(int[] arr, int i, int j) {
        //Try swapping without extra variable
        if (i != j) { // Check if the indices are different to avoid unnecessary swapping when i and j are the same
            arr[i] = arr[i] ^ arr[j];
            arr[j] = arr[i] ^ arr[j];
            arr[i] = arr[i] ^ arr[j];
        }
    }

    /* This function is same in both iterative and 
       recursive*/
    int partition(int[] arr, int l, int h) {
        int pivot = arr[h];
        int i = (l - 1); // index of smaller element
        for (int j = l; j <= h - 1; j++) {

            if (arr[j] <= pivot) {
                i++;

                // swap arr[i] and arr[j]
                swap(arr, i, j);
            }
        }

        int temp = arr[i + 1];
        arr[i + 1] = arr[h];
        arr[h] = temp;

        return i + 1;
    }

    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int[] arr, int l, int h) {
        //Try using Stack Data Structure to remove recursion.
        Stack<Integer> stack = new Stack<>();
        stack.push(l);
        stack.push(h);
        while (!stack.isEmpty()) {
            h = stack.pop();
            l = stack.pop();
            int pi = partition(arr, l, h);

            if (pi - 1 > l) {
                stack.push(l);
                stack.push(pi - 1);
            }

            if (pi + 1 < h) {
                stack.push(pi + 1);
                stack.push(h);
            }

        }

    }

    // A utility function to print contents of arr 
    void printArr(int[] arr, int n) {
        int i;
        for (i = 0; i < n; ++i)
            System.out.print(arr[i] + " ");
    }

    // Driver code to test above 
    public static void main(String args[]) {
        IterativeQuickSort ob = new IterativeQuickSort();
        int[] arr = {4, 3, 5, 2, 1, 3, 2, 3};
        ob.QuickSort(arr, 0, arr.length - 1);
        ob.printArr(arr, arr.length);
    }
} 