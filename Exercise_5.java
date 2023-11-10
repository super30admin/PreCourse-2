// Time Complexity : O(nLogn)
// Space Complexity : O(logn)
// Did this code successfully run on Leetcode :
// Any problem you faced while coding this :

class IterativeQuickSort {
    void swap(int arr[], int i, int j)
    {
        //Try swapping without extra variable
        int temp = arr[j];
        arr[j] = arr[i];
        arr[i] = temp;
    }

    /* This function is same in both iterative and
       recursive*/
    int partition(int arr[], int l, int h)
    {
        //Compare elements and swap.
        int pi = arr[h];
        int i = (l-1);
        for(int j=l;j<=h-1;j++)
        {
            if(arr[j]<pi)
            {
                i++;
                swap(arr,i,j);
            }
        }
        swap(arr,i+1,h);
        return i+1;
    }

    // Sorts arr[l..h] using iterative QuickSort
    void QuickSort(int arr[], int l, int h)
    {
        //Try using Stack Data Structure to remove recursion.
        int[] stk = new int[h-l+1];
        int top = -1;
        stk[++top] = l;
        stk[++top] = h;

        while(top >= 0 )
        {
            h=stk[top--];
            l=stk[top--];
            int pi = partition(arr,l,h);

            if (pi - 1 > l) {
                stk[++top] = l;
                stk[++top] = pi - 1;
            }

            // If there are elements on right side of pivot,
            // then push right side to stack
            if (pi + 1 < h) {
                stk[++top] = pi + 1;
                stk[++top] = h;
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
        int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 };
        ob.QuickSort(arr, 0, arr.length - 1);
        ob.printArr(arr, arr.length);
    }
}
