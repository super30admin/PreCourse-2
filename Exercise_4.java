class MergeSort
{
    // Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]
    //Time complexiy of merge sort is o(nlogn)
    void merge(int arr[], int l, int m, int r)
    {
        //Your code here
        //Calculate the size of 2 sub arrays

        int sizeFirstSubarr = m - l + 1;
        int sizeSecondSubarr = r - m;
        int leftArr[] = new int[sizeFirstSubarr];
        int rightArr[]  = new int[sizeSecondSubarr];

        for (int i=0; i < sizeFirstSubarr; ++i) {
            leftArr[i] = arr[l+i];
        }

        for (int j=0; j<sizeSecondSubarr; ++j) {
            rightArr[j] = arr[m+1+j];
        }

        int i = 0;
        int j = 0;
        int k = l;

        while( i < sizeFirstSubarr && j < sizeSecondSubarr) {

            if (leftArr[i] <= rightArr[j]) {
                arr[k] = leftArr[i];
                i++;
            }
            else {
                arr[k] = rightArr[j];
                j++;
            }
            k++;
        }

        while (i < sizeFirstSubarr) {
            arr[k] = leftArr[i];
            i++;
            k++;
        }

        while (j < sizeSecondSubarr) {

            arr[k] = rightArr[j];
            j++;
            k++;
        }
    }

    // Main function that sorts arr[l..r] using
    // merge()
    void sort(int arr[], int l, int r)
    {
        //Write your code here
        //Call mergeSort from here
        if (l < r) {
            int middleElem = l + (r-l) / 2;

            sort(arr,l,middleElem);
            sort(arr,middleElem + 1, r);

            //Call mergeSort from here
            merge(arr,l,middleElem,r);
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