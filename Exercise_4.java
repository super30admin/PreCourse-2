class MergeSort
{
    // Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]
    void merge(int arr[], int l, int m, int r)
    {
        //Your code here
        // finding sizes of two sub arrays
        int n1 = m-l+1;
        int n2 = r-m;

        //creating two temp arrays

        int L[] = new int[n1];
        int R[] = new int[n2];

        for (int i = 0; i < n1; i++) {
            L[i] = arr[l+i];

        }
        for (int i = 0; i < n2; i++) {
            R[i] = arr[m + 1 + i];
        }


        /*Merging the temp arrays*/

        // initial indexes of first and second sub arrays

        int first = 0;
        int second = 0;

        // initial indexes of merged sub array

        int k = l ;

        while(first < n1 && second < n2){

            if (L[first] <= R[second]){
                arr[k] = L[first];
                first ++;
            }else {
                arr[k] = R[second];
                second++;
            }
            k++;
        }

        /* Copying the remaining elements of L[] if there any left */
        while (first < n1){
            arr[k] = L[first];
            first++;
            k++;
        }

        /* Copying the remaining elements of L[] if there any left */
        while(second < n2){
            arr[k] = R[second];
            second++;
            k++;
        }


    }

    // Main function that sorts arr[l..r] using
    // merge()
    void sort(int arr[], int l, int r)
    {
        //Write your code here
        //Call mergeSort from here

        if(l < r){
            int m = (l + r) / 2 ;
            sort (arr,l, m);
            sort (arr,m+1,r);
            merge (arr, l, m, r);
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