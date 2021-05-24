//Time Complexity: O(n^2)
//Space Complexity: O(n) -> for storing low and high values after partition method returns an index value.
// //In the worst case, At max 2n values might be stored (assuming every index is returned as pivot element after partition fn call)
class IterativeQuickSort {
    void swap(int arr[], int i, int j) {
        // Try swapping without extra variable
        // Using bitwise XOR ; property: x^y^x= y; but if x and y are same then x^y  will be zero. So, avoid swapping same numbers.
        if(arr[i]==arr[j])
            return;
        arr[i] = arr[i] ^ arr[j];
        arr[j] = arr[i] ^ arr[j];
        arr[i] = arr[i] ^ arr[j];
    }

    /*
     * This function is same in both iterative and recursive
     */
    int partition(int arr[], int l, int h) {
        // Compare elements and swap.
        int pivot = arr[h];
        int left = l, r = h;

        while (left < r) {
            while (arr[left] < pivot && left < r)
                left++;
            while (arr[r] >= pivot && left < r)
                r--;

            if (left < r)
                swap(arr, left, r);

        }
        swap(arr, left, h);
        return left;
    }

    // Sorts arr[l..h] using iterative QuickSort
    void QuickSort(int arr[], int l, int h) {
        // Try using Stack Data Structure to remove recursion.
        int index = 0, low = 0, high = 0;
        low = l;
        high = h;
        Stack<Integer> stack = new Stack<Integer>();
        stack.push(low);
        stack.push(high);
        while (stack.size() > 0) {
            high = stack.pop();
            low = stack.pop();
            if (low >= high)
                continue;
            index = partition(arr, low, high);
            stack.push(low);
            stack.push(index - 1);
            stack.push(index + 1);
            stack.push(high);

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