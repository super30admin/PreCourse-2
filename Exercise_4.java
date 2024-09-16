class MergeSort 
{
    // Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]
    void merge(int arr[], int l, int m, int r)
    {
        //Your code here
        // Create 2 sub-arrays out of arr[]  by finding the sizes
        int n1 = m - l + 1;
        int n2 = r - m;

        // Create 2 sub-arraays using the calculated size
        int leftArray[] = new int[n1];
        int rightArray[] = new int[n2];

        //copy data to the sub-arrays
        for (int i = 0; i < n1; i++)
            leftArray[i] = arr[l + i];
        for (int j = 0; j < n2; j++)
            rightArray[j] = arr[m + 1 + j];

        // Initial indexes of first and second sub-arrays
        int i = 0, j = 0;

        // Initial index of merged sub-array array
        int k = l;
        while (i < n1 && j < n2) {
            //compare leftArray[i] with rightArray[j] i
            if (leftArray[i] <= rightArray[j]) {
                arr[k] = leftArray[i];
                i++;
            }
            else {
                arr[k] = rightArray[j];
                j++;            }
            k++;
        }

        // Copy if there are any remaining elements left in leftArray[] to arr[k]
        while (i < n1) {
            arr[k] = leftArray[i];
            i++;
            k++;
        }

        // Copy if there are any remaining elements in  right array to arr
        while (j < n2) {
            arr[k] = rightArray[j];
            j++;
            k++;
        }
    }

    // Main function that sorts arr[l..r] using
    // merge()
    void sort(int arr[], int l, int r)
    {
        //Write your code here
        if (l < r) {
            // Find the middle point
            int m = l + (r - l) / 2;

            // Sort first half using start(left) to middle
            sort(arr, l, m);
            //Sort second half from middle+1 as middle already done to end(right)
            sort(arr, m + 1, r);
            //Call mergeSort from here
            merge(arr, l, m, r);
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