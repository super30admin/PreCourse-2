import java.util.Arrays;

class MergeSort {
    /* A utility function to print array of size n */
    static void printArray(int arr[]) {
        int n = arr.length;
        for (int i = 0; i < n; ++i)
            System.out.print(arr[i] + " ");
        System.out.println();
    }

    // Driver method
    public static void main(String args[]) {
        int arr[] = {12, 11, 13, 5, 6, 7};

        System.out.println("Given Array");
        printArray(arr);

        MergeSort ob = new MergeSort();
        ob.sort(arr, 0, arr.length - 1);

        System.out.println("\nSorted array");
        printArray(arr);
    }

    // Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]
    void merge(int arr[], int l, int m, int r) {
        int[] leftArray = Arrays.copyOfRange(arr, l, m + 1);
        int[] rightArray = Arrays.copyOfRange(arr, m + 1, r + 1);

        int i = l;
        int j = 0;
        int k = 0;

        while (j < leftArray.length && k < rightArray.length) {
            if (leftArray[j] <= rightArray[k]) {
                arr[i] = leftArray[j];
                j++;
            } else {
                arr[i] = rightArray[k];
                k++;
            }
            i++;
        }

        while (j < leftArray.length) {
            arr[i] = leftArray[j];
            j++;
            i++;
        }
        while (k < rightArray.length) {
            arr[i] = rightArray[k];
            k++;
            i++;
        }
    }

    // Main function that sorts arr[l..r] using
    // merge()
    void sort(int arr[], int l, int r) {
        if (l==r) {
            return;
        }

        int m = (l + r) / 2;
        sort(arr, l, m);
        sort(arr, m + 1, r);
        merge(arr, l, m, r);
    }
} 