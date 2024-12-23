import java.util.Arrays;
import java.util.Stack;

class IterativeQuickSort {
    int pivot=0;
    void swap(int arr[], int i, int j)
    {
        int temp=arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    /* This function is same in both iterative and
       recursive*/
    int partition(int arr[], int l, int h)
    {
        int temp = 0;
        int i = l;
        int j = h-1;

        pivot = arr[h];

        //Write code here for Partition and Swap
        while (i <= j) {
            if (arr[i] > pivot && arr[j] <= pivot) {
                swap(arr, i, j);
                i++;
                j--;
            } else {
                if (arr[i] <= pivot) {
                    i++;
                }
                if (arr[j] > pivot) {
                    j--;
                }
            }
        }
        swap(arr, i, h);
        System.out.println(Arrays.toString(arr));
        System.out.println(j);
        return i;
    }

    // Sorts arr[l..h] using iterative QuickSort
    void QuickSort(int arr[], int l, int h)
    {
            Stack<Integer> low = new Stack<>();
            Stack<Integer> high = new Stack<>();
            int index=0;
            low.push(l);
            high.push(h);
            while (!low.empty() && !high.empty()) {
                l = low.pop();
                h = high.pop();
                System.out.println("l "+l);
                System.out.println("h "+h);
                if (l < h) {
                    index = partition(arr, l, h);
                    System.out.println("Index "+index);
                    low.push(l);
                    high.push(index - 1);
                    low.push(index + 1);
                    high.push(h);
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
        int arr[] = {4,3,5,2,1,3,2,3};
        ob.QuickSort(arr, 0, arr.length - 1);
        ob.printArr(arr, arr.length);
    }
}
