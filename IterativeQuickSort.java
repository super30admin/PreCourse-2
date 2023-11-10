// Time Complexity :  O(nlogn) for best and avergae case 
//                 :  O(n^2) for worst case ; where n is the no. of elements in the array
// Space Complexity : O(n) as stack is created 

//Code:

class IterativeQuickSort {
    void swap(int arr[], int i, int j) {
        // Try swapping without extra variable
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    /*
     * This function is same in both iterative and
     * recursive
     */
    int partition(int arr[], int low, int high) {
        // Compare elements and swap.
        int i = low, j = low;
        int pivot = arr[high]; // taking pivot as the element at high index as pivot will reach at its correct
                               // position after partition
        while (i <= high) {
            if (arr[i] <= pivot) { // if arr[i] is smaller than pivot then we need to swap the elements and
                                   // increement their indexes
                swap(arr, i, j);
                i++;
                j++;
            } else {
                i++;
            }
        }
        return (j - 1);
    }

    // Sorts arr[l..h] using iterative QuickSort
    void QuickSort(int arr[], int l, int h) {
        int[] stack = new int[h - l + 1];
        int top = -1; // initializing top of stack

        stack[++top] = l; // first increementing top and then pushing values of l and h
        stack[++top] = h;

        while (top >= 0) { // loop will continue till stack is not empty

            h = stack[top--]; // popping l and h
            l = stack[top--];

            int p = partition(arr, l, h); // getting index of pivot element

            if (p - 1 > l) { // If there are elements on left side of pivot, then pushing index of first and
                             // last index of left side to stack
                stack[++top] = l;
                stack[++top] = p - 1;
            }

            if (p + 1 < h) {            // If there are elements on right side of pivot, then pushing index of first and
                // last index of right side to stack
                stack[++top] = p + 1;
                stack[++top] = h;
            }
        }

    }

    // A utility function to print contents of arr
    void printArr(int arr[], int n) {
        int i;
        for (i = 0; i < n; i++)
            System.out.print(arr[i] + " ");
    }

    // Driver code to test above
    public static void main(String args[]) {
        IterativeQuickSort ob = new IterativeQuickSort();
        int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 };
        ob.QuickSort(arr, 0, arr.length - 1);
        ob.printArr(arr, arr.length);
    }
}