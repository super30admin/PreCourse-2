// Time Complexity : O(n^2)
// Space Complexity : O(n)
class IterativeQuickSort {
    void swap(int arr[], int i, int j) {
        // Swapping without extra variable
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
        int pindex = l;
        // Traverse through array and place elements less than pivot to the left
        for (int i = l; i < h; i++) {
            if (arr[i] < pivot) {
                swap(arr, i, pindex);// swap current element with element at pindex
                pindex++;
            }
        }
        // swap the pivot to its corrected sorted position
        swap(arr, pindex, h);
        return pindex;
    }

    // Sorts arr[l..h] using iterative QuickSort
    void QuickSort(int arr[], int l, int h) {
        // Try using Stack Data Structure to remove recursion.
        int[] a = new int[h - l + 1];
        int top = -1;
        // pushing l and h
        a[++top] = l;
        a[++top] = h;
        while (top >= 0) {
            h = a[top--];
            l = a[top--];
            int p = partition(arr, l, h);
            if (p - 1 > l) {
                a[++top] = l;
                a[++top] = p - 1;
            }
            if (p + 1 < h) {
                a[++top] = p + 1;
                a[++top] = h;
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