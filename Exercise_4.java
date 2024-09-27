class MergeSort {

    void merge(int arr[], int l, int m, int r) {
        int temp[] = new int[r - l + 1];
        int i1 = l;
        int i2 = m + 1;
        int index = 0;
        while (i1 <= m && i2 <= r) {
            if (arr[i1] <= arr[i2]) {
                temp[index++] = arr[i1++];
            } else {
                temp[index++] = arr[i2++];
            }
        }
        while (i1 <= m) {
            temp[index++] = arr[i1++];
        }
        while (i2 <= r) {
            temp[index++] = arr[i2++];
        }

        index = 0;
        for (int i = l; i <= r; i++) {
            arr[i] = temp[index++];
        }

    }

    // Time complexity : O(nlogn)
    // Space Complexity : O(n)
    void sort(int arr[], int l, int r) {
        if (l < r) {
            int mid = (l + r) / 2;
            sort(arr, l, mid);
            sort(arr, mid + 1, r);
            merge(arr, l, mid, r);
        }
    }

    /* A utility function to print array of size n */
    static void printArray(int arr[]) {
        int n = arr.length;
        for (int i = 0; i < n; ++i)
            System.out.print(arr[i] + " ");
        System.out.println();
    }

    // Driver method
    public static void main(String args[]) {
        int arr[] = { 12, 11, 13, 5, 6, 7, 5, 5, 5, 5, 5, 2 };

        System.out.println("Given Array");
        printArray(arr);

        MergeSort ob = new MergeSort();
        ob.sort(arr, 0, arr.length - 1);

        System.out.println("\nSorted array");
        printArray(arr);
    }
}