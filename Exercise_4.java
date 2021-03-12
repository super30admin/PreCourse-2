class MergeSort
{
    // Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]
    void merge(int arr[], int l, int m, int r)
    {
      int[] helper = new int[arr.length];
      for (int i=l; i<=r; i++){
          helper[i] = arr[i];
      }
      int i = l;
      int j = m + 1;
      for (int k=l; k <= r; k++) {
          if (i > m) arr[k] = helper[j++];
          else if (j > r) arr[k] = helper[i++];
          else if (helper[j] < helper[i]) arr[k] = helper[j++];
          else arr[k] = helper[i++];
      }
    }

    // Main function that sorts arr[l..r] using
    // merge()
    void sort(int arr[], int l, int r)
    {
      if (l < r) {
          int m = (l + r)/2;
          sort(arr, l, m);
          sort(arr, m+1, r);
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
