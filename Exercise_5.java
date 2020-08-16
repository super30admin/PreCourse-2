import java.util.Stack;

class IterativeQuickSort {
    void swap(int arr[], int i, int j) {
        // Try swapping without extra variable

        // Your code here
        // tried this didint work
        // arr[i] =arr[i]^arr[j];
        // arr[j] =arr[i]^arr[j];
        // arr[i] = arr[i]^arr[j];

        // Your code here
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;

    }

    /*
     * This function is same in both iterative and recursive
     */
    int partition(int arr[], int low, int high) {
        int pivot = arr[high];

        // index of smaller element
        int i = (low - 1);
        for (int j = low; j <= high - 1; j++) {

            if (arr[j] <= pivot) {
                i++;
                swap(arr, i, j);
            }
        }

        swap(arr, i + 1, high);

        return i + 1;
    }

    // Sorts arr[l..h] using iterative QuickSort
    void QuickSort(int arr[], int l, int h) {
        // Try using Stack Data Structure to remove recursion.

        Stack<Integer> st = new Stack<>();
        st.push(l);
        st.push(h);

        while (!st.isEmpty()) {

            h = st.pop();
            l = st.pop();

            int p = partition(arr, l, h);

            if (p - 1 > l) {
                st.push(l);
                st.push(p - 1);
            }
            if (p + 1 < h) {
                st.push(p + 1);
                st.push(h);
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