/**
 * Time Complexity : O(n log n)
 * Space Complexity: O(log n)
 * Any problem you faced while coding this : Difficult to comprehend, studied from online resources to implement
 */
class IterativeQuickSort {
    void swap(int arr[], int i, int j)
    {
	//Try swapping without extra variable
        if (i != j) {
            arr[i] = arr[i] + arr[j];
            arr[j] = arr[i] - arr[j];
            arr[i] = arr[i] - arr[j];
        }
    }

    /* This function is same in both iterative and
       recursive*/
    int partition(int arr[], int l, int h)
    {
        //Compare elements and swap.
        // Pivot center element
        int pivot = arr[l + (h - l) / 2];
        while (l <= h) {
            while (arr[l] < pivot)
                l++;
            while (arr[h] > pivot)
                h--;
            if (l <= h) {
                swap(arr, l, h);
                l++;
                h--;
            }
        }
        return l;
    }

    // Sorts arr[l..h] using iterative QuickSort
    void QuickSort(int arr[], int l, int h)
    {
        //Try using Stack Data Structure to remove recursion.
        if (l >= h)
            return;
        int[] stack = new int[h - l + 1];
        int top = -1;
        stack[++top] = l;
        stack[++top] = h;

        // keep popping stack until it's empty
        while (top >= 0) {
            h = stack[top--];
            l = stack[top--];
            int pivotIndex = partition(arr, l, h);
            if (pivotIndex - 1 > l) {
                stack[++top] = l;
                stack[++top] = pivotIndex - 1;
            }
            if (pivotIndex < h) {
                stack[++top] = pivotIndex;
                stack[++top] = h;
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