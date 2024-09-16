class MergeSort {
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) {
        //Your code here
        int size1 = m - 1 + 1;
        int size2 = r - m;
        int[] firstSubArray = new int[size1];
        int[] secondSubArray = new int[size2];

        for (int i = 0; i < size1; ++i) {
            firstSubArray[i] = arr[l + i];
        }
        for (int j = 0; j < size2; ++j) {
            secondSubArray[j] = arr[m + 1 + j];
        }

        int i = 0, j = 0, k = 1;
        while (i <= size1 && j <= size2) {

            if (firstSubArray[i] <= secondSubArray[j]) {
                arr[k++] = firstSubArray[i++];
            } else {
                arr[k++] = secondSubArray[j++];
            }
        }
        for (; i < size1; i++) {
            arr[k++] = firstSubArray[i];
        }
        for (; j < size2; j++) {
            arr[k++] = secondSubArray[j];
        }

    }

    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) {
        //Write your code here
        //Call mergeSort from here
        if (l < r) {
            int mid = l + (r - 1) / 2;
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
        int arr[] = {12, 11, 13, 5, 6, 7};

        System.out.println("Given Array");
        printArray(arr);

        MergeSort ob = new MergeSort();
        ob.sort(arr, 0, arr.length - 1);

        System.out.println("\nSorted array");
        printArray(arr);
    }
} 