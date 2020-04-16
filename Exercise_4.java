//Time Complexity:O(nlogn)
//Space Complexity:O(n)
class MergeSort
{
 
    void merge(int arr[], int l, int m, int r)
    {
        int sl = m - l + 1;
        int sr = r - m;
        
        int L[] = new int [sl];
        int R[] = new int [sr];

        
        for (int i=0; i<sl; ++i)
            L[i] = arr[l + i];
        for (int j=0; j<sr; ++j)
            R[j] = arr[m + 1+ j];


        int i = 0, j = 0;

        int k = l;
        while (i < sl && j < sr)
        {
            if (L[i] <= R[j])
            {
                arr[k] = L[i];
                i++;
            }
            else
            {
                arr[k] = R[j];
                j++;
            }
            k++;
        }

   
        while (i < sl)
        {
            arr[k] = L[i];
            i++;
            k++;
        }
        
        while (j < sr)
        {
            arr[k] = R[j];
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
            int m=(l+r)/2;
            sort(arr,l,m);
            sort(arr,m+1,r);
            merge(arr,l,m,r);
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