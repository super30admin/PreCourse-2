class MergeSort {
    // Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]
    void merge(int arr[], int s, int mid, int e) {
        int len1 = mid - s + 1;
        int len2 = e - mid;
        int[] arr1 = new int[len1];
        int[] arr2 = new int[len2];

        // copy elements in these arrays;
        int originalArrayIndex = s;
        for (int i = 0; i < len1; i++) {
            arr1[i] = arr[originalArrayIndex++];
        }

        for (int i = 0; i < len2; i++) {
            arr2[i] = arr[originalArrayIndex++];
        }

        originalArrayIndex = s;

        int idx1 = 0;
        int idx2 = 0;
        while (idx1 < len1 && idx2 < len2) {
            if (arr1[idx1] < arr2[idx2]) {
                arr[originalArrayIndex++] = arr1[idx1++];
            } else {
                arr[originalArrayIndex++] = arr2[idx2++];
            }
        }

        while (idx1 < len1) {
            arr[originalArrayIndex++] = arr1[idx1++];
        }

        while (idx2 < len2) {
            arr[originalArrayIndex++] = arr2[idx2++];
        }
    }

    // Main function that sorts arr[l..r] using
    // merge()
    void sort(int arr[], int s, int e) {
        if (s >= e)
            return;

        int mid = s + (e - s) / 2;
        // left Part
        sort(arr, s, mid);
        // right part
        sort(arr, mid + 1, e);
        merge(arr, s, mid, e);
    }

}

public class Exercise_4 {

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