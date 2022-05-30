class MergeSort {
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) {
        //Your code here
        // Create Aux array and copy all the elements to it
        int[] aux = new int[arr.length];

        for (int k = l; k <= r; k++) aux[k] = arr[k];

        int i = l;
        int j = m + 1;

        for (int k = l; k <= r; k++) {

            if (i > m) arr[k] = aux[j++];
            else if (j > r) arr[k] = aux[i++];
            else if (aux[i] <= aux[j]) arr[k] = aux[i++];
            else arr[k] = aux[j++];
        }
    }

    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) {
        //Write your code here
        //Call mergeSort from here

        if (r <= l) return;
        // Sort Both the half
        int mid = l + (r - l) / 2;
        sort(arr, l, mid);
        sort(arr, mid + 1, r);

        // merge two sorted subarray
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
        int arr[] = {12, 11, 13, 5, 6, 7};

        System.out.println("Given Array");
        printArray(arr);

        MergeSort ob = new MergeSort();
        ob.sort(arr, 0, arr.length - 1);

        System.out.println("\nSorted array");
        printArray(arr);
    }
} 