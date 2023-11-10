// Time Complexity : O(n log n)
// Space Complexity : O(log n)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : No

class IterativeQuickSort {
    void swap(int arr[], int i, int j)
    {
        arr[i] = arr[i] + arr[j];
        arr[j] = arr[i] - arr[j];
        arr[i] = arr[i] - arr[j];
    }

    int partition(int arr[], int l, int h)
    {
        /// make the last element of the array as pivot
        int pivot = arr[h];

        // initialize i = -1;
        int i = l - 1;

        // traverse the array and swap elements at positions i & j for every element at j less than pivot
        for(int j = l; j <= h -1; j++){
            if(arr[j] < pivot){
                i++;
                swap(arr, i, j);
            }
        }
        // Put the pivot in its ordered position
        swap(arr, i + 1, h);
        return i+1;
    }

    // Sorts arr[l..h] using iterative QuickSort
    void QuickSort(int arr[], int l, int h)
    {
        // Create a stack
        int[] stack = new int[h - l + 1];

        // initialize top of stack
        int top = -1;

        // push initial values of l and h to stack
        stack[++top] = l;
        stack[++top] = h;

        // Pop elements from stack until it is empty
        while (top >= 0) {
            // Pop h and l
            h = stack[top--];
            l = stack[top--];

            // Set pivot to correct position
            int p = partition(arr, l, h);

            // Push left hand side elements to pivot, if any
            if (p - 1 > l) {
                stack[++top] = l;
                stack[++top] = p - 1;
            }

            // Push right hand side elements to pivot, if any
            if (p + 1 < h) {
                stack[++top] = p + 1;
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