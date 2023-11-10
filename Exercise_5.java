import java.util.Stack;

// Time complexity: O(nlogn), logn passes for each n partitions.
//Space Complexity is O(n) due to new stack DS creation.
// Class with 2 indices to replicate the process as done with an Array for quickSort logic.
class Indices {
    private int idx1;
    private int idx2;

    Indices(int idx1, int idx2) {
        this.idx1 = idx1;
        this.idx2 = idx2;
    }

    public int getIdx1() {
        return idx1;
    }

    public int getIdx2() {
        return idx2;
    }
}

class IterativeQuickSort {
    void swap(int arr[], int i, int j) {
        // Try swapping without extra variable
        // Swapping of elements using bit math ^.
        if (arr[i] == arr[j])
            return;
        arr[i] = arr[i] ^ arr[j];
        arr[j] = arr[i] ^ arr[j];
        arr[i] = arr[i] ^ arr[j];
    }

    /*
     * This function is same in both iterative and
     * recursive
     */
    int partition(int arr[], int l, int h) {
        // Compare elements and swap.
        int pivot = arr[h];
        int startIdx = l;
        for (int idx = l; idx < h; idx++) {
            if (arr[idx] <= pivot) {
                swap(arr, idx, startIdx++);
            }
        }
        swap(arr, startIdx, h);
        return startIdx;
    }

    // Sorts arr[l..h] using iterative QuickSort
    void QuickSort(int arr[], int l, int h) {
        // Try using Stack Data Structure to remove recursion.
        Stack<Indices> st = new Stack<>();
        l = 0;
        h = arr.length - 1;
        st.push(new Indices(l, h));

        while (!st.empty()) {
            l = st.peek().getIdx1();
            h = st.peek().getIdx2();
            st.pop();

            int pivot = partition(arr, l, h);

            if (pivot - 1 > l) {
                st.push(new Indices(l, pivot - 1));
            }
            if (pivot + 1 > h) {
                st.push(new Indices(pivot + 1, h));
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
        System.out.println();
    }
}