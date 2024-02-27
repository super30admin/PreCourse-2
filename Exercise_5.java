import java.util.Stack;
class Exercise_5{
    // Function to swap two elements in the array without using an extra variable
    void swap(int arr[], int i, int j) {
        if (i != j) {
            arr[i] = arr[i] + arr[j];
            arr[j] = arr[i] - arr[j];
            arr[i] = arr[i] - arr[j];
        }
    }

    // Function to partition the array and return the pivot index
    int partition(int arr[], int l, int h) {
        int pivot = arr[h];
        int i = (l - 1);

        for (int j = l; j < h; j++) {
            if (arr[j] <= pivot) {
                i++;
                swap(arr, i, j);
            }
        }
        swap(arr, i + 1, h);
        return i + 1;
    }

    // Function to sort the array using QuickSort iteratively
    void QuickSort(int arr[], int l, int h) {
        // Create a stack to store subarray boundaries
        Stack<Integer> stack = new Stack<>();
        // Push initial values of l and h to the stack
        stack.push(l);
        stack.push(h);

        // Keep popping from stack while it's not empty
        while (!stack.isEmpty()) {
            // Pop h and l from stack
            h = stack.pop();
            l = stack.pop();

            // Set pivot element at its correct position
            int p = partition(arr, l, h);

            // If there are elements on the left side of the pivot, push them to the stack
            if (p - 1 > l) {
                stack.push(l);
                stack.push(p - 1);
            }

            // If there are elements on the right side of the pivot, push them to the stack
            if (p + 1 < h) {
                stack.push(p + 1);
                stack.push(h);
            }
        }
    }

    // Function to print the array
    void printArr(int arr[], int n) {
        for (int i = 0; i < n; ++i)
            System.out.print(arr[i] + " ");
    }

    // Driver code to test the sorting
    public static void main(String args[]) {
        Excercise_5 ob = new Excercise_5();
        int arr[] = {4, 3, 5, 2, 1, 3, 2, 3};
        int n = arr.length;
        ob.QuickSort(arr, 0, n - 1);
        ob.printArr(arr, n);
    }
}
