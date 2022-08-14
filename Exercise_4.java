class MergeSort
{
    // Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]
    void merge(int arr[], int l, int m, int r)
    {
        int s1 = m - l + 1;
        int s2 = r - m;

        int[] arr1 = new int[s1];
        int[] arr2 = new int[s2];


        for(int i = 0 ; i < s1 ; i++){
            arr1[i] = arr[i + l];
        }

        for(int i = 0; i < s2 ; i++){
            arr2[i] = arr[i + m + 1];
        }

        int i = 0, j = 0;
        int k = l;
        while(i < s1 && j < s2){
            if(arr1[i] < arr2[j]){
                arr[k] = arr1[i];
                i++;
                k++;
            }else{
                arr[k] = arr2[j];
                j++;
                k++;
            }
        }

        while(i < s1){
            arr[k] = arr1[i];
            i++;
            k++;
        }

        while(j < s2){
            arr[k] = arr2[j];
            j++;
            k++;
        }
    }

    // Main function that sorts arr[l..r] using
    // merge()
    void sort(int arr[], int l, int r)
    {
        //Stopping condition is important for recurssion
        if (l < r) {
            int mid = (l + r) / 2;
            sort(arr, l, mid);
            sort(arr, mid + 1, r);
            merge(arr, l, mid, r);
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