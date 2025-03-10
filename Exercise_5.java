// Time Complexity :
// Best/Average Case: O(n log n) where n is the size of the array
// Worst Case: O(n^2) , when pivot is always the smallest or largest element)

// Space Complexity: O(log n)
import java.util.Stack;

class IterativeQuickSort {
    void swap(int arr[], int i, int j)
    {
	//Try swapping without extra variable
        if(i == j ) return;
        arr[i] = arr[i] + arr[j];
        arr[j] = arr[i] - arr[j];
        arr[i] = arr[i] - arr[j];
    }

    /* This function is same in both iterative and
       recursive*/
    int partition(int arr[], int l, int h)
    {
        //Write code here for Partition and Swap
        int pivot = arr[h];
        int i = l - 1;

        for(int j = i+1 ;j < h; j++) {
            //if element is smaller or equal to pivot, swap
            if(arr[j] <= pivot) {
                swap(arr, ++i, j);
            }
        }
        // final swap with the pivot
        swap(arr, i+1, h);

        // returns partition index
        return i+1;

    }

    // Sorts arr[l..h] using iterative QuickSort
    void QuickSort(int arr[], int l, int h)
    {
        //Try using Stack Data Structure to remove recursion.
        Stack<Integer> stack = new Stack<>();

        // Push to the stack
        stack.push(l);
        stack.push(h);

        // popping from the stack until it is empty
        while (!stack.isEmpty()) {

            h = stack.pop();
            l = stack.pop();

            // Partition the array
            int partIndex = partition(arr, l, h);

            // If elements on the left side, push  to stack
            if (partIndex - 1 > l) {
                stack.push(l);
                stack.push(partIndex - 1);
            }

            // If elements on the right side, push to stack
            if (partIndex + 1 < h) {
                stack.push(partIndex + 1);
                stack.push(h);
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