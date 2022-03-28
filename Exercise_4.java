//time complexity - O(nlogn)

class MergeSort
{
    // Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]
    void merge(int arr[], int l, int m, int r)
    {
        //size of arrays for merging
        int n1= m-l+1;
        int n2= r-m;

        //temp array for merging
        int[] left = new int[n1];
        int[] right = new int[n2];

        //copy array to temp array
        for(int i =0 ;i<n1;i++)
            left[i] = arr[l+i];

        for(int j =0 ;j<n2;j++)
            right[j] = arr[m+j+1];


        int i =0 ,j=0;
        int k =l;
        //comparing and merging array
        while(i<n1 && j<n2)
        {
            if(left[i] <= right[j])
            {
                arr[k]=left[i];
                i++;
            }
            else {
                arr[k]=right[j];
                j++;
            }
            k++;
        }

        while(i<n1)
        {
            arr[k]=left[i];
            i++;
            k++;
        }

        while(j<n2)
        {
            arr[k]=right[j];
            j++;
            k++;
        }
    }



    // Main function that sorts arr[l..r] using
    // merge()
    void sort(int arr[], int l, int r)
    {
        if(l<r)
        {
            int mid = (l+r)/2;
            sort(arr , l , mid);
            sort(arr , mid+1,r);
            merge(arr , l , mid,r);
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