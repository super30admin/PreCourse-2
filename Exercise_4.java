import java.util.ArrayList;
import java.util.List;

class MergeSort {
    // Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]
    void merge(int arr[], int l, int mid, int r) {
        // Your code here
        List<Integer> list = new ArrayList<>();
        int l_itr = l;
        int r_itr = mid + 1;
        while (l_itr <= mid && r_itr <= r) {
            if (arr[l_itr] <= arr[r_itr]) {
                list.add(arr[l_itr]);
                l_itr++;
            } else {
                list.add(arr[r_itr]);
                r_itr++;
            }
        }
        while (l_itr <= mid) {
            list.add(arr[l_itr]);
            l_itr++;
        }

        while (r_itr <= r) {
            list.add(arr[r_itr]);
            r_itr++;
        }

        for (int i = l; i <= r; i++) {
            arr[i] = list.get(i - l);
        }
    }

    // Main function that sorts arr[l..r] using
    // merge()
    void sort(int arr[], int l, int r) {
        // Write your code here
        // Call mergeSort from here
        if (l == r) {
            return;
        }
        int mid = l + (r - l) / 2;
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