class MergeSort
{
    // Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]
    void merge(int arr[], int l, int m, int r)
    {
        //Your code here
        int n1 = m-l+1;
        int n2 = r - m;

        int lArr[] = new int[n1];
        int rArr[] = new int[n2];

        for(int i=0; i<n1; i++){
            lArr[i] = arr[l+i];
        }
        for(int j=0; j<n2; j++){
            rArr[j] = arr[m+1+j];
        }

        int i=0, j=0, k=l;

        while(i<n1 && j<n2){
            if(lArr[i]<=rArr[j]) {
                arr[k++] = lArr[i++];
            }
            else {
                arr[k++] = rArr[j++];
            }
        }

        //copy remaining elements from temp array to main arr
        while(i<n1){
            arr[k++] = lArr[i++];
        }

        while(j<n2){
            arr[k++] = rArr[j++];
        }
    }

    // Main function that sorts arr[l..r] using
    // merge()
    void sort(int arr[], int l, int r)
    {
        //Write your code here
        //Call mergeSort from here
        if(l < r){
            int mid = (l+r)/2;

            sort(arr, l, mid);
            sort(arr,mid+1, r);

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
        int arr[] = {12, 11, 13, 5, 6, 7, -200, 20, -4, 30, 8, 15, -5};

        System.out.println("Given Array");
        printArray(arr);

        MergeSort ob = new MergeSort();
        ob.sort(arr, 0, arr.length-1);

        System.out.println("\nSorted array");
        printArray(arr);
    }
}