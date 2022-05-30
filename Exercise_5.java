import java.util.Stack;

class IterativeQuickSort {
    void swap(int arr[], int i, int j) {
        //Try swapping without extra variable
        arr[i] = arr[i] + arr[j];
        arr[j] = arr[i] - arr[j];
        arr[i] = arr[i] - arr[j];
    }

    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) {
        //Compare elements and swap.

        int i = lo;
        int j = hi + 1;

        while (true) {

            while (arr[++i] < arr[lo]) if (i == hi) break;

            while (arr[lo] < arr[--j]) if (j == lo) break;

            // Check if i and j crossed
            if (j <= i) break;

            swap(arr, i, j);

        }

        // swap with the pivot element
        swap(arr, lo, j);

        return j;

    }

    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) {
        //Try using Stack Data Structure to remove recursion.
        if (high <= low) return;

        Stack<Integer> st = new Stack<>();
        st.push(low);
        st.push(high);

        while (!st.isEmpty()) {

            high = st.pop();
            low = st.pop();

            int j = partition(arr, low, high);

            // check if pivot and low has elements
            // If Yes then push the elements in Stack
            if (low < j - 1) {
                st.push(low);
                st.push(j - 1);
            }

            // check if pivot and high has elements
            // If Yes then push the elements in Stack
            if (j + 1 < high) {
                st.push(j + 1);
                st.push(high);
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