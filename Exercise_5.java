/**
 * Time Complexity : best case: O(n log n); worst case O(n2)
 * Space Complexity: best case: O(log n); worst case O(n)
 * Did this code successfully run on Leetcode : Yes, https://leetcode.com/problems/sort-an-array/
 *
 * Any problem you faced while coding this : Recursion and Iterative is difficult to comprehend; had to study from GFG to implement
 */
class IterativeQuickSort {
    void swap(int[] arr, int i, int j) {
        //Try swapping without extra variable
        if (i != j) {
            arr[i] = arr[i] + arr[j];
            arr[j] = arr[i] - arr[j];
            arr[i] = arr[i] - arr[j];
        }
//        int temp = arr[i];
//        arr[i] = arr[j];
//        arr[j] = temp;
    }

    /* This function is same in both iterative and 
       recursive*/
    int partition(int[] arr, int l, int h) {
        //Compare elements and swap.
        int pivot = arr[l + (h - l) / 2];          // Pivot center element
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
    void QuickSort(int[] arr, int l, int h) {
        if (l >= h)
            return;
        int[] stack = new int[h - l + 1];       // Stack to handle recursive nature
        int top = -1;                           // top of empty stack
        stack[++top] = l;                       // Insert low and high into stack
        stack[++top] = h;

        // keep popping stack until it's empty
        while (top >= 0) {
            h = stack[top--];       // process for popped l and h
            l = stack[top--];
            int pivotIndex = partition(arr, l, h);  // partition around current pivot
            if (pivotIndex - 1 > l) {                   // push pivotIndex onto stack for left half
                stack[++top] = l;
                stack[++top] = pivotIndex - 1;
            }
            if (pivotIndex < h) {               // push pivotIndex onto stack for right half
                stack[++top] = pivotIndex;
                stack[++top] = h;
            }
        }
    }

    // A utility function to print contents of arr 
    void printArr(int[] arr, int n) {
        int i;
        for (i = 0; i < n; ++i)
            System.out.print(arr[i] + " ");
    }

    // Driver code to test above 
    public static void main(String[] args) {
        IterativeQuickSort ob = new IterativeQuickSort();
        int[] arr = {4, 3, 5, 2, 1, 3, 2, 3};
        ob.QuickSort(arr, 0, arr.length - 1);
        ob.printArr(arr, arr.length);
    }
} 