class MergeSort
{

    /**
     * Merges two subarrays of arr[]. First subarray is arr[l..m] Second subarray is arr[m+1..r]
     * @param arr array of integers
     * @param l l index in an array
     * @param m middle index of l and r
     * @param r right index in array
     */
    void merge(int arr[], int l, int m, int r)
    {
        //Assume l to m is sorted and m to r is sorted and now we have to merge two sorted arrays;
        int p1=m-l+1;
        int p2=r-m;
        int count=0;

        //create 2 arrays of size p1 and p2
        int A[]=new int[p1];
        int B[]=new int[p2];

        //copy data from l to m in array A
        for(int i=l;i<=m;i++){
            A[count++]=arr[i];
        }
         count=0;
        //copy data from m+1 to r in array A
        for(int i=m+1;i<=r;i++){
            B[count++]=arr[i];
        }
        p1=0;
        p2=0;
        //Merge two sorted arrays in arr
        while(p1<A.length && p2<B.length){
            if(A[p1]<B[p2]) {
                arr[l++] = A[p1++];
            }
            else{
                arr[l++]=B[p2++];
            }
        }
        //copy remaining elements of array A
        while(p1<A.length)
            arr[l++] = A[p1++];

        //copy remaining elements of array B
        while(p2<B.length)
            arr[l++]=B[p2++];

    }



    /**
     * Merge sort function that sorts arr[l..r]
     * @param arr array of integres
     * @param l left index in array
     * @param r right index in array
     */
    /*Time complexity:o(n log n)
      Space complexity :o(n) As we are using temporary arrays to while merging and sorting
     */
    void sort(int arr[], int l, int r)
    {
        if(l<r){
            int m=(l+r)/2;
            sort(arr,l,m);
            sort(arr,m+1,r);
            merge(arr,l,m,r);
        }
    }

    /*  */

    /**
     * A utility function to print array of size n
     * @param arr
     */
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
        int arr[] = {12, 11, 13, 5, 6, 7,7};

        System.out.println("Given Array");
        printArray(arr);

        MergeSort ob = new MergeSort();
        ob.sort(arr, 0, arr.length-1);

        System.out.println("\nSorted array");
        printArray(arr);
    }
}