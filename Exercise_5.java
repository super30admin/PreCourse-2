// Operation:          Iterative Quicksort
// Time Complexity:            n*n
// Space Complexity:            n
// Yes, this code ran successfully
// Yes, I faced problem in implementing iterative approach using Stack and thus took reference from internet

class IterativeQuickSort {
    void swap(int arr[], int i, int j)
    {
	    //Try swapping without extra variable
        arr[i] = arr[j] + (arr[j]=arr[i]) - arr[j] ;
    }

    /* This function is same in both iterative and recursive*/
    int partition(int arr[], int l, int h)
    {
        //Compare elements and swap.

        int i = l;
        int j = h;

        int pivot = arr[h] ;                     // setting up pivot
        while(i<j)
        {
            while(arr[i]<=pivot && i<h)          // leaving values on left hand side(correct side) of pivot
                i++;
            while(arr[j]>=pivot && j>l)           // leaving values on right hand side(correct side) of pivot
                j--;
            if(i<j)
                swap(arr,i,j);
        }
        swap(arr,i,h);                           // swapping pivot to its correct position
        return i;
    }

    // Sorts arr[l..h] using iterative QuickSort
    void QuickSort(int arr[], int l, int h)
    {
        //Try using Stack Data Structure to remove recursion.
        if(l<h)
        {
            int[] stack = new int[h - l + 1];           // creating stack using array
            int top = -1;
            stack[++top] = l;                           // pushing lower index in stack
            stack[++top] = h;                           // pushing higher index in stack
            while (top >= 0) {
                h = stack[top--];                       // popping higher index from stack
                l = stack[top--];                       // popping lower index from stack

                int j = partition(arr, l, h);           // setting up correct index of pivot

                if (l < j - 1) {                        // adding lower and higher indexes of subarray on left side of pivot
                    stack[++top] = l;
                    stack[++top] = j - 1;
                }

                if (j + 1 < h) {                        // adding lower and higher indexes of subarray on right side of pivot
                    stack[++top] = j + 1;
                    stack[++top] = h;
                }
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