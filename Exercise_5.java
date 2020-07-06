import java.util.Stack;

/*Time Complexity : O(n logn)
 Space Complexity : O(N), using stack to keep pointers

 Your code here along with comments explaining your approach: While sorting using recursion,
 we store the start and end in memory stack. So instead of using process memory, we keep
 external stack to store start and end of the sub-array. At first, find the pivot index and keep pivot
 at pivot index. Once pivot is fixed, divide the array in left half and right half. Store the start and
 end indices of left and right half in the stack. Using start and end index, sort the sub arrays.
*/

class IterativeQuickSort {
    void swap(int arr[], int i, int j) {
        if (i != j) {
            arr[j] = arr[i] + arr[j];
            arr[i] = arr[j] - arr[i];
            arr[j] = arr[j] - arr[i];
        }
    }

    /* This function is same in both iterative and
       recursive*/
    int partition(int arr[], int low, int high) {
        int pivotIndex = high;
        for (int i = low; i < high; i++) {
            if (arr[i] < arr[pivotIndex]) {
                swap(arr, low, i);
                low += 1;
            }
        }
        swap(arr, pivotIndex, low);
        pivotIndex = low;
        return pivotIndex;
    }

    // Sorts arr[l..h] using iterative QuickSort
    void QuickSort(int arr[], int low, int high) {
        //Try using Stack Data Structure to remove recursion.
        Stack<Integer> stack = new Stack<>();
        stack.push(low);
        stack.push(high);

        while (!stack.isEmpty()) {
            int upper = stack.pop();
            int lower = stack.pop();
            if (lower < upper) {
                int pivotIndex = partition(arr, lower, upper);
                if (lower < pivotIndex - 1) {
                    stack.push(lower);
                    stack.push(pivotIndex - 1);
                }
                if (pivotIndex + 1 < upper) {
                    stack.push(pivotIndex + 1);
                    stack.push(upper);
                }
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
        int arr[] = {4, 3, 5, 2, 1, 3, 2, 3};
        ob.QuickSort(arr, 0, arr.length - 1);
        ob.printArr(arr, arr.length);
    }
} 