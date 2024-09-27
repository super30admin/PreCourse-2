
public class MergeSort {
    // Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]
    void merge(int arr[], int l, int m, int r) {
        int lenOfArray1 = m - l + 1;
        int lenOfArray2 = r - m;

        int[] subArr1 = new int[lenOfArray1];
        int[] subArr2 = new int[lenOfArray2];

        for (int i = 0; i < lenOfArray1; i++) {
            subArr1[i] = arr[l + i];
        }
        for (int i = 0; i < lenOfArray2; i++) {
            subArr2[i] = arr[m + 1 + i];
        }

        int i = 0;
        int j = 0;
        int k = l;

        while (i < lenOfArray1 && j < lenOfArray2) {
            if (subArr1[i] < subArr2[j]) {
                arr[k] = subArr1[i];
                i++;
            } else {
                arr[k] = subArr2[j];
                j++;
            }
            k++;
        }

        while (i < lenOfArray1) {
            arr[k] = subArr1[i];
            i++;
            k++;
        }
        while (j < lenOfArray2) {
            arr[k] = subArr2[j];
            j++;
            k++;
        }
    }

    void sort(int arr[], int l, int r) {
        if (l < r) {
            int mid = l + (r - l) / 2;

            sort(arr, l, mid);
            sort(arr, mid + 1, r);

            merge(arr, l, mid, r);
        }
    }

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