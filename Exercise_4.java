//time complexity is O(n*Logn)
//space complexity O(n)+O(Logn) which is O(n)
class MergeSort {
    // Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]
    void merge(int arr[], int l, int m, int r) {
        // Your code here
        int p1 = m - l + 1;
        int p2 = r - m;
        int le[] = new int[p1];
        int ri[] = new int[p2];
        for (int i = 0; i < p1; ++i)
            le[i] = arr[l + i];
        for (int j = 0; j < p2; ++j)
            ri[j] = arr[m + 1 + j];
        int i = 0, j = 0;
        int k = l;
        while (i < p1 && j < p2) {
            if (le[i] <= ri[j]) {
                arr[k] = le[i];
                i++;
            } else {
                arr[k] = ri[j];
                j++;
            }
            k++;
        }
        while (i < p1) {
            arr[k] = le[i];
            i++;
            k++;
        }
        while (j < p2) {
            arr[k] = ri[j];
            j++;
            k++;
        }
    }

    // Main function that sorts arr[l..r] using
    // merge()
    void sort(int arr[], int l, int r) {
        // Write your code here
        // Call mergeSort from here
        if (l < r) {
            int m = l + (r - l) / 2;
            sort(arr, l, m);
            sort(arr, m + 1, r);
            merge(arr, l, m, r);
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
        int arr[] = { 12, 11, 13, 5, 6, 7 };

        System.out.println("Given Array");
        printArray(arr);

        MergeSort ob = new MergeSort();
        ob.sort(arr, 0, arr.length - 1);

        System.out.println("\nSorted array");
        printArray(arr);
    }
}