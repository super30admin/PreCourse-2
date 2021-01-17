class MergeSort
{
    // Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]
    void merge(int arr[], int l, int m, int r)
    {
        /*  Time Complexity: O(n)
            Space Complexity: O(n)
         */
        //Your code here
        int arr1Length = m-l+1;
        int arr2Length = r - m;
        int arr1[] = new int[arr1Length];
        int arr2[] = new int[arr2Length];
        for (int i=0; i<arr1Length ; i++)
            arr1[i] = arr[l+i];
        for( int i=0; i<arr2Length; i++)
            arr2[i] = arr[m+1+i];

        int k = l, i=0, j=0;
        while (i < arr1Length && j < arr2Length) {
            if (arr1[i] <= arr2[j]) {
                arr[k] = arr1[i];
                i++;
            }
            else {
                arr[k] = arr2[j];
                j++;
            }
            k++;
        }

        while (i < arr1Length) {
            arr[k] = arr1[i];
            i++;
            k++;
        }

        while (j < arr2Length) {
            arr[k] = arr2[j];
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

        /*  Time Complexity:
            We will be having log n levels. At which we call merge() which is O(n) every time.
           Therefore time complexity is O(nlogn)

           Best, Worst, Average cases: O(nlogn)

         */

        if(l < r){
            int mid = (l+r)/2;
            sort(arr,l,mid);
            sort(arr,mid+1,r);
            merge(arr,l,mid,r);
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