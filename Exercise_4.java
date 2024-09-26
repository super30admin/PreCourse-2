class MergeSort
{
    // Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]
    void merge(int arr[], int l, int m, int r)
    {
       //Your code here
       int i=l;
       int j=m+1;
       int k=l;
       int b[]= new int[6];

        while(i<=m && j<=r)
        {
            if(arr[i]<=arr[j])
            {
                b[k]=arr[i];
                i++;
            }
            else{
                b[k]=arr[j];
                j++;
            }
            k++;
        }
        if(i>m) {
            while(j<=r)
                {b[k]=arr[j];
                j++;
                k++; }
            }
        else{
            while(i<=m){
                b[k]=arr[i];
                i++;
                k++;
            }
        }
        for(k=l;k<=r;k++){
            arr[k]=b[k];
        }
    }

    // Main function that sorts arr[l..r] using
    // merge()
    void sort(int arr[], int l, int r)
    {
        int m;
	//Write your code here
        if(l<r)
        {
            m=(l+r)/2;
            sort(arr,l,m);
            sort(arr,m+1,r);
            merge(arr,l,m,r);
        }
        //Call mergeSort from here
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