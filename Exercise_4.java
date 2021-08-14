class MergeSort
{

    // Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]
    void merge(int arr[], int l, int m, int r)
    {
        int a1 = m - l + 1;
        int a2 = r - m;

        int[] t1 = new int[a1];
        int[] t2 = new int[a2];

        for (int i = 0; i < a1; i++)
        {
            t1[i] = arr[i + l];
        }
        for (int j = 0; j < a2; j++)
        {
            t2[j] = arr[j + m + 1];
        }

        int i = 0, j = 0;
        int idx = l;

        while (i < a1 && j < a2)
        {
            if (t1[i] <= t2[j])
            {
                arr[idx] = t1[i];
                idx++;
                i++;
            }
            else
            {
                arr[idx] = t2[j];
                idx++;
                j++;
            }
        }

        while (i < a1)
        {
            arr[idx] = t1[i];
            idx++;
            i++;
        }

        while (j < a2)
        {
            arr[idx] = t2[j];
            idx++;
            j++;
        }

    }

    // Main function that sorts arr[l..r] using
    // merge()
    void sort(int arr[], int l, int r)
    {
        if (l < r)
        {
            int m = l + (r - l) / 2;
            sort(arr, l, m);
            sort(arr, m + 1, r);
            merge(arr, l, m, r);
        }
    }

    /* A utility function to print array of size n */
    static void printArray(int arr[])
    {
        int n = arr.length;
        for (int i = 0; i < n; ++i)
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
        ob.sort(arr, 0, arr.length - 1);

        System.out.println("\nSorted array");
        printArray(arr);
    }
}

/*
// Time Complexity : O(nLogn)
// Space Complexity : O(n)
// Did this code successfully run on Leetcode :
// Any problem you faced while coding this : While merging two array
 */