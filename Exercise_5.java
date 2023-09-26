class IterativeQuickSort {
    void swap(int arr[], int i, int j) {
//        arr[i] = arr[i] ^ arr[j];
//        arr[j] = arr[i] ^ arr[j];
//        arr[i] = arr[i] ^ arr[j];
// Swapping using bit manipulation gives errors
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    /* This function is same in both iterative and
       recursive*/
    int partition(int arr[], int low, int high) {
        //Compare elements and swap.
        int lastSmall = low - 1;
        int pivot = arr[high];
        while (low < high) {
            if (arr[low] <= pivot) {
                lastSmall++;
//                if (arr[lastSmall] != arr[low]) {
                    swap(arr, lastSmall, low);
//                }
            }
            low++;
        }
        swap(arr, lastSmall + 1, high);

        return lastSmall + 1;
    }

    // Sorts arr[l..h] using iterative QuickSort
    void QuickSort(int arr[], int l, int h) {
        //Try using Stack Data Structure to remove recursion.top
        int stack[] = new int[h - l + 1];

        int top = -1;

        stack[++top] = l;
        stack[++top] = h;

        while (top >= 0) {
            h = stack[top--];
            l = stack[top--];

            int pivot = partition(arr, l, h);

            if (pivot - 1 > l) {
                stack[++top] = l;
                stack[++top] = pivot - 1;
            }
            if (pivot + 1 < h) {
                stack[++top] = pivot + 1;
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
        int arr[] = {4, 3, 5, 2, 1, 3, 2, 3};
        ob.QuickSort(arr, 0, arr.length - 1);
        ob.printArr(arr, arr.length);
    }
}