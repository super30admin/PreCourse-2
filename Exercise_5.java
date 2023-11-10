// Time Complexity : O(nlogn)

// Space Complexity : O(logn) -> depth of stack

// Did this code successfully run on Leetcode : yes

// Any problem you faced while coding this :No

// Your code here along with comments explaining your approach
/* we select last element as pivot element. Once pivot assigned, set i as low and j as high index.
 * increment index through the array from left(i) till we find a greater value than pivot and decrement index from right(j) till we find a smaller value than pivot.
 * if we find smaller and greater value we swap i and j. if i and j cross each other we swap the pivot value with the j index and return the j value as partition index.
 * Then we sort the remaining by using the partition index.
 * Here for iterative Quicksort I have used stack data structure to call the left and right side of the partition index to sort.
 */
import java.util.Stack;

class IterativeQuickSort {
    void swap(int arr[], int i, int j) {
        // Try swapping without extra variable
        // if the values at i and j are same, no need to swap them
        if (arr[i] != arr[j]) {
            arr[i] = arr[i] + arr[j];
            arr[j] = arr[i] - arr[j];
            arr[i] = arr[i] - arr[j];
        }

    }

    /*
     * This function is same in both iterative and
     * recursive
     */
    int partition(int arr[], int l, int h) {
        // Compare elements and swap.
        int pivot = arr[h];
        int i = l, j = h;
        // iterate through the array till i and j don't intersect with each other.
        while (i < j) {

            // increment i till we find a value greater than pivot element
            while (arr[i] <= pivot && i < j) {
                i++;
            }

            // decrement j till we find value smaller than pivot element
            while (arr[j] >= pivot && i < j) {
                j--;
            }

            // swap element at index i and j
            swap(arr, i, j);
        }

        // swap element at i and high(pivot) to get the partition index
        swap(arr, i, h);

        return i;
    }

    // Sorts arr[l..h] using iterative QuickSort
    void QuickSort(int arr[], int l, int h) {
        // Try using Stack Data Structure to remove recursion.
        Stack<Integer> stack = new Stack<Integer>();
        // push l and h to the stack to find the initila partition index
        stack.push(l);
        stack.push(h);
        // run the below logic till the stack is empty, we use stack to remove
        // recursion.
        while (!stack.isEmpty()) {
            int high = stack.pop();
            int low = stack.pop();
            // run partition function to generate the index to split.
            int j = partition(arr, low, high);

            // split the array on the left and right side of the partition satisfying the
            // greater than and less than condition for split.
            if (j - 1 > low) {
                stack.push(low);
                stack.push(j - 1);

            }
            if (j + 1 < high) {
                stack.push(j + 1);
                stack.push(high);
            }

        }

    }

    // A utility function to print contents of arr
    void printArr(int arr[], int n) {
        int i;
        for (i = 0; i < n; ++i)
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