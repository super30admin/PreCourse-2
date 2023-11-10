import java.util.Stack;

class IterativeQuickSort {
    // Time Complexity: Worst Case O(n^2), Average Case O(n * log n)
    // Space Complexity: Worst Case O(n), Average Case O(log n)

    void swap(int arr[], int i, int j)
    {
	//Try swapping without extra variable
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    /* This function is same in both iterative and
       recursive*/
    int partition(int arr[], int l, int h)
    {
        //Compare elements and swap.
        int i = l;
        int j = h + 1;
        int p = arr[l];

        while (i < j) {
            do {
                i++;
            } while (i < j  && arr[i] <= p);

            do {
                j--;
            } while (j >= i && arr[j] >= p);

            if (i < j) {
                swap(arr, i ,j);
            }
        }
        swap(arr, l, j);
        return j;

    }

    // Sorts arr[l..h] using iterative QuickSort
    void QuickSort(int arr[], int l, int h)
    {
        //Try using Stack Data Structure to remove recursion.
        Stack<Integer> s = new Stack();
        s.add(l);
        s.add(h);
        while (!s.isEmpty()) {
            h = s.pop();
            l = s.pop();
            int p = partition(arr, l, h);
            if (p - 1 > l) {
                s.push(l);
                s.push(p - 1);
            }

            if (p + 1 < h) {
                s.push(p + 1);
                s.push(h);
            }

        }

    }

    // A utility function to print contents of arr
    void printArr(int arr[], int n)
    {
        int i;
        for (i = 0; i < n; ++i)
            System.out.print(arr[i] + " ");
    }

    // Driver code to test above
    public static void main(String args[])
    {
        IterativeQuickSort ob = new IterativeQuickSort();
        int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 };
        ob.QuickSort(arr, 0, arr.length - 1);
        ob.printArr(arr, arr.length);
    }
}