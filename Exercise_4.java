class MergeSort
{
    // Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]
    void merge(int arr[], int l, int m, int r)
    {
        int leftend=(m+1)-l;
        int rightend=r-m;
        int [] templeft = new int[leftend];
        int[] tempright = new int[rightend];
        for(int i=0;i<leftend;i++)
       {
            templeft[i]=arr[l+i];
       }
        for(int j=0;j<rightend;j++)
        {
            tempright[j]=arr[m+1+j];
        }
        int i=0;
        int j=0,k=l;
        while(i<leftend && j <rightend)
        {
            if(templeft[i]<=tempright[j])
            {
                arr[k++]=templeft[i++];
            }
            else
            {
                arr[k++]=tempright[j++];
            }
        }
        while(i<leftend)
        {
            arr[k++]=templeft[i++];
        }
        while(j<rightend)
        {
            arr[k++]=tempright[j++];
        }
    }
    // Main function that sorts arr[l..r] using
    // merge()
    void sort(int arr[], int l, int r)
    {
        if(l<r)
        {
            int mid = (l+r)/2;
            sort(arr,l,mid);
            sort(arr,mid+1,r);
            merge(arr,l,mid,r);
        }

	//Write your code here
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