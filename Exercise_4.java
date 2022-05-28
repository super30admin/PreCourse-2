class MergeSort
{

    // Time Complexity: O(n* log n)
    // Space Complexity: O(n)


    // Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]


    void merge(int arr[], int l, int m, int r)
    {
       //Your code here
        int[] c = new int[r - l + 1];
        int i = l;
        int j = m + 1;
        int k = 0;
        while (i <= m && j <= r) {
            if (arr[i] <= arr[j]) {
                c[k++] = arr[i];
                i++;
            } else {
                c[k++] = arr[j];
                j++;
            }
        }

        while (i <= m) {
            c[k++] = arr[i++];
        }

        while (j <= r) {
            c[k++] = arr[j++];
        }

        for (k = 0; k < c.length; k++) {
            arr[l++] = c[k];
        }

    }

    // Main function that sorts arr[l..r] using
    // merge()
    void sort(int arr[], int l, int r)
    {
	//Write your code here
        //Call mergeSort from here
        if (l < r) {
            int m = l + (r - l)/2;
            sort(arr, l, m);
            sort(arr, m + 1, r);
            merge(arr, l, m , r);
        }
    }

    /* A utility function to print array of size n */
    static void printArray(int arr[])
    {
        int n = arr.length;
        for (int i=0; i<n; ++i)
            System.out.print(arr[i] + " ");
        System.out.println();
    }

    // Driver method
    public static void main(String args[])
    {
        int arr[] = {12, 11, 13, 5, 6, 7};

        System.out.println("Given Array");
        printArray(arr);

        MergeSort ob = new MergeSort();
        ob.sort(arr, 0, arr.length-1);

        System.out.println("\nSorted array");
        printArray(arr);
    }
}