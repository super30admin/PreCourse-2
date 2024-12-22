import java.util.ArrayList;
import java.util.List;

class MergeSort {
    // Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]
    void merge(int arr[], int l, int m, int r) {
        // Your code here
        List<Integer> temp = new ArrayList<>();
        int leftPtr = l;
        int rightPtr = m + 1;

        while (leftPtr <= m && rightPtr <= r) {
            if (arr[leftPtr] <= arr[rightPtr]) {
                temp.add(arr[leftPtr]);
                leftPtr++;
            } else {
                temp.add(arr[rightPtr]);
                rightPtr++;
            }
        }

        while (leftPtr <= m) {
            temp.add(arr[leftPtr++]);
        }

        while (rightPtr <= r) {
            temp.add(arr[rightPtr++]);
        }

        for (int i = l; i <= r; i++) {
            arr[i] = temp.get(i - l);
        }
    }

    // Main function that sorts arr[l..r] using
    // merge()
    void sort(int arr[], int l, int r) {
        // Write your code here
        // Call mergeSort from here
        if (l >= r)
            return;

        int mid = (l + r) / 2;
        sort(arr, l, mid);
        sort(arr, mid + 1, r);
        merge(arr, l, mid, r);
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
        int arr[] = { 12, 11, 13, 5, 6, 7 };

        System.out.println("Given Array");
        printArray(arr);

        MergeSort ob = new MergeSort();
        ob.sort(arr, 0, arr.length - 1);

        System.out.println("\nSorted array");
        printArray(arr);
    }
}