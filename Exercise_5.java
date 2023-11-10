import java.util.Stack;

class Exercise_5 {
    void swap(int arr[], int i, int j) {
        // Try swapping without extra variable
        if (i == j) {
            return;
        }
        arr[i] = arr[i] + arr[j];
        arr[j] = arr[i] - arr[j];
        arr[i] = arr[i] - arr[j];
    }

    /*
     * This function is same in both iterative and
     * recursive
     */
    int partition(int arr[], int low, int high) {
        // Compare elements and swap.
        int pivot = arr[high];
        int pivotIndex = high;
        while (low < high) {
            while (arr[low] <= pivot && low < high) {
                low++;
            }

            while (arr[high] >= pivot && low < high) {
                high--;
            }
            swap(arr, low, high);
            System.out.println(arr);
            System.out.println("-------------------------");
        }
        swap(arr, low, pivotIndex);

        return low;
    }

    // Sorts arr[l..h] using iterative QuickSort
    void QuickSort(int arr[], int low, int high) {
        // Try using Stack Data Structure to remove recursion.
        Stack<Integer> sortStack = new Stack<Integer>();
        sortStack.push(low);
        sortStack.push(high);

        while (!sortStack.isEmpty()) {
            int end = sortStack.pop();
            int start = sortStack.pop();

            if (end - start <= 0) {
                continue;
            }

            int partitionIndex = partition(arr, start, end);
            // array elements before partitionIndex
            sortStack.push(start);
            sortStack.push(partitionIndex-1);

            sortStack.push(partitionIndex);
            sortStack.push(end);

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
        Exercise_5 ob = new Exercise_5();
        int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 };
        ob.QuickSort(arr, 0, arr.length - 1);
        ob.printArr(arr, arr.length);
    }
}