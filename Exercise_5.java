// Time Complexity :  0(nLog(n)); // Should be similar to the recursive Q.S, but should be faster since stack call and function activation calss would be avoided.
// Space Complexity : O(nLog(n)); // Similar to recursive Q.S since the core partitioning algorithm is same.
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : determining complexity
import java.util.Stack;

class IterativeQuickSort {
    void swap(int arr[], int i, int j) {
        //Try swapping without extra variable
        // Added equality check to prevent same reference object swap.
        if (arr[i] != arr[j]) {
            arr[i] = arr[i] + arr[j];
            arr[j] = arr[i] - arr[j];
            arr[i] = arr[i] - arr[j];
        }
    }

    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) {
        //Compare elements and swap.
        int pivot = h;
        int divider = -1;
        int i = 0;
        for (i = 0; i < h; i++) {
            System.out.println("Checking i with pivot : " + arr[i] + "," + arr[pivot] + " divider : " + divider);
            if (arr[i] <= arr[pivot]) {
                //  divider point to elems less than pivot; so increment divider and swap;
                divider++;
                swap(arr, i, divider);
            }
            printArr(arr, arr.length);
        }
        swap(arr, divider + 1, pivot);
        return divider + 1;
    }

    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) {
        //Try using Stack Data Structure to remove recursion.
        Stack<Integer> left_stack = new Stack<>();
        // Sorting the left side of the stack and pushing the pivot
        while (l < h) {
            int pivot = partition(arr, l, h);
            System.out.println("Pivot idx is : " + pivot);
            left_stack.push(pivot);
            h = pivot - 1;
        }
        // Popping pivot and sorting the right side of the stack
        h = arr.length - 1;
        while (!left_stack.isEmpty()) {
            int pivot = left_stack.pop();
            System.out.println("Pivot idx is : " + pivot);
            l = pivot + 1;
            partition(arr, l, h);
        }
        System.out.println("Stack Size : " + left_stack.size());
    }

    // A utility function to print contents of arr 
    void printArr(int arr[], int n) {
        int i;
        for (i = 0; i < n; ++i)
            System.out.print(arr[i] + " ");
        System.out.println();
    }

    // Driver code to test above 
    public static void main(String args[]) {
        IterativeQuickSort ob = new IterativeQuickSort();
        int arr[] = {4, 3, 5, 2, 1, 3, 2, 3};
        System.out.println("original array");
        ob.printArr(arr, arr.length);
        ob.QuickSort(arr, 0, arr.length - 1);
        ob.printArr(arr, arr.length);
    }
} 