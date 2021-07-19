import java.util.Stack;

class IterativeQuickSort {
    void swap(int arr[], int i, int j)
    {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    /* This function is same in both iterative and
       recursive*/
    int partition(int arr[], int l, int h){
        int pivot = arr[h];

        int i = (l - 1);
        for (int j = l; j <= h - 1; j++) {
            if (arr[j] <= pivot) {
                i++;

                swap(arr, i, j);

            }
        }

        int temp = arr[i + 1];
        arr[i + 1] = arr[h];
        arr[h] = temp;

        return i + 1;
    }

    void QuickSort(int arr[], int l, int h)
    { 
        Stack<Integer> st = new Stack<>();
        int top = -1;

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