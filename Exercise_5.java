import java.util.Stack;

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
    int partition(int arr[], int l, int h) {
        // Compare elements and swap.
        // take last element as a pivot
        int pivot = arr[h];
        // left pointer will be 1 less than low because here we are using do while loop
        // so it will increase by one.
        int i = l - 1;
        // right pointer will be start from high.
        int j = h;
        // if left pointer crosses rigth pointer it means that there is no element on
        // left side that is greater than pivot and same as there is no element on the
        // right side that is less than pivot
        while (i < j) {

            // here we check first element that is less than pivot from right side.
            do {
                j--;
            } while (arr[j] >= pivot);
            // here we check first element that is greater than pivot from left side.

            do {

                i++;
            } while (arr[i] < pivot);
            // once we find element that is greater than pivot from left side and less than
            // pivot from ride side we swap them.
            if (i < j) {
                swap(arr, i, j);
            }

        }

        // if loops break then we find right position for the pivot element. and we put
        // pivot on the right position.
        swap(arr, i, h);
        // return the position of the pivot element.
        return i;
    }

    // Sorts arr[l..h] using iterative QuickSort
    void QuickSort(int arr[], int l, int h) {
        // Try using Stack Data Structure to remove recursion.
        Stack<Integer> stk = new Stack<>();

        // push initial values of l and h to stack
        stk.push(l);
        stk.push(h);

        while (!stk.isEmpty()) {
            // Pop h and l
            h = stk.pop();
            l = stk.pop();

            // set pivot element at its correct position
            // in sorted array and store pivot index in p
            int p = partition(arr, l, h);

            // If there are elements on left side of pivot,
            // then push left side to stack
            if (p - 1 > l) {
                stk.push(l);
                stk.push(p - 1);
            }

            // If there are elements on right side of pivot,
            // then push right side to stack
            if (p + 1 < h) {
                stk.push(p + 1);
                stk.push(h);

            }
        }
    }

    // A utility function to print contents of arr
    void printArr(int arr[], int n) {
        int i;
        System.out.println("sorted array");
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