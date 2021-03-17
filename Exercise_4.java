class MergeSort
{
    // Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]
    void merge(int arr[], int l, int m, int r)
    {
        int leftp=l;
        int rightp=m+1;
        int[] mini_sort=new int[r-l+1];
        int sort_index=0;
        while(leftp<=m && rightp<=r)
        {
           if(arr[leftp]<arr[rightp])
           {
               mini_sort[sort_index]=arr[leftp];
               sort_index++;
               leftp++;
           }
           else
           {
               mini_sort[sort_index]=arr[rightp];
               sort_index++;
               rightp++;
           }
        }
        while(leftp<=m)
        {
            mini_sort[sort_index]=arr[leftp];
            sort_index++;
            leftp++;
        }
        while(rightp<=r)
        {
            mini_sort[sort_index]=arr[rightp];
            sort_index++;
            rightp++;
        }
        for(int i=l;i<=r;i++)
        {
            arr[i]=mini_sort[i-l];
        }
    }

    // Main function that sorts arr[l..r] using
    // merge()
    void sort(int arr[], int l, int r)
    {
        if(l<r)
        {
            int mid=l+(r-l)/2;
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
