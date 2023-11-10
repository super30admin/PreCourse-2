import java.util.Stack;

// Time Complexity : Best case O(nLogN), worst case: O(n^2)
// Space Complexity :
// Did this code successfully run on Leetcode : NO, for the given input, i am getting output -> 1 2 2 0 0 3 4 5
// Any problem you faced while coding this : I am not pretty clear if this could be implemented with the pivot as mid point or not.
class IterativeQuickSort {
    void swap(int arr[], int i, int j)
    {
	//Try swapping without extra variable
        arr[i] = arr[i] + arr[j]; // Add both x + y to x, arr[i] -> x + y, arr[j] -> y
        arr[j] = arr[i] - arr[j]; // Subtract y from x + y to give x assign it to arr[j], arr[i] -> x + y, arr[j] -> x
        arr[i] = arr[i] - arr[j]; // subtract x from x + y to give y, assign it to arr[i], arr[i] -> y, arr[j] -> x

    }

    /* This function is same in both iterative and
       recursive*/
    int partition(int arr[], int l, int h)
    {
        //Compare elements and swap.
        int pivot = arr[h];
        int i = (l-1);

        for (int j = l; j < h; j++) {
            if(arr[j] <= pivot) {
                i++;
                swap(arr, j, i);
            }
        }

        swap(arr, i+1, h);
        return i+1;
    }

    // Sorts arr[l..h] using iterative QuickSort
    void QuickSort(int arr[], int l, int h)
    {
        //Try using Stack Data Structure to remove recursion.
        int stack[] = new int[h-l+1];
        int top = -1;

        stack[++top] = l;
        stack[++top] = h;

        while (top >= 0) {

            h = stack[top];
            top--;
            l = stack[top];
            top--;

            // Calling the partition function
            int partition = partition(arr, l, h);

            // Push left side of pivot to the stack
            if(partition - 1 > l) {
                top++;
                stack[top] = l;
                top++;
                stack[top] = partition-1;
            }

            // Push right side of pivot to  the stack
            if(partition + 1 < h) {
                top++;
                stack[top] = partition + 1;
                top++;
                stack[top] = h;
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