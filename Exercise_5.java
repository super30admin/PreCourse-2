class IterativeQuickSort
{

    void swap(int arr[], int i, int j)
    {
        //Try swapping without extra variable
        int x = arr[i];
        int y = arr[j];
        x = x + y;
        y = x - y;
        x = x - y;

        arr[i] = x;
        arr[j] = y;

    }

    /* This function is same in both iterative and
       recursive*/
    int partition(int arr[], int l, int h)
    {
        //Compare elements and swap.
        int pivot = arr[h];
        int i = l - 1;

        for (int j = l; j <= h - 1; j++)
        {
            if (arr[j] <= pivot)
            {
                i++;
                swap(arr, i, j);
            }
        }
        swap(arr, i + 1, h);
        return (i + 1);
    }

    // Sorts arr[l..h] using iterative QuickSort
    void QuickSort(int arr[], int l, int h)
    {
        //Try using Stack Data Structure to remove recursion.
        int[] tmpArray = new int[h - l + 1];
        int idx = -1;

        tmpArray[++idx] = l;
        tmpArray[++idx] = h;

        while (idx >= 0)
        {
            h = tmpArray[idx--];
            l = tmpArray[idx--];

            int par = partition(arr, l, h);

            if (par - 1 > l)
            {
                tmpArray[++idx] = l;
                tmpArray[++idx] = par - 1;
            }

            if (par + 1 < h)
            {
                tmpArray[++idx] = par + 1;
                tmpArray[++idx] = h;
            }
        }
    }

    // A utility function to print contents of arr
    void printArr(int arr[], int n)
    {
        int i;
        for (i = 0; i < n; ++i)
            System.out.print(arr[i] + " ");
    }

    // Driver code to test above
    public static void main(String args[])
    {
        IterativeQuickSort ob = new IterativeQuickSort();
        int arr[] = {4, 3, 5, 2, 1, 3, 2, 3};
        ob.QuickSort(arr, 0, arr.length - 1);
        ob.printArr(arr, arr.length);
    }
}

/*
// Time Complexity : O(nLogn)
// Space Complexity : O(n)
// Did this code successfully run on Leetcode :
// Any problem you faced while coding this : In QuickSort() method
 */
