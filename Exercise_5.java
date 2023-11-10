import java.util.Stack;

class IterativeQuickSort {
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
        int pivot  = arr[h];
        int indexPivot = h;

        while(l < h) {
            while(arr[l] <= pivot && l < h) {
                l++;
            }
            while(arr[h] >= pivot && l < h) {
                h--;
            }
            swap(arr, l, h);
        }

        swap(arr, l, indexPivot);
        return l;
    }

    // Sorts arr[l..h] using iterative QuickSort
    void QuickSort(int arr[], int l, int h)
    {
        //Try using Stack Data Structure to remove recursive*on.

        Stack<Integer> visited = new Stack<>();

        visited.push(h);
        visited.push(l);

        while(!visited.isEmpty()){

            int low = visited.pop();
            int high = visited.pop();

            int idx = partition(arr, low, high);

            if (idx>low) {
                // there are elements on left to pivot
                visited.push(idx-1);
                visited.push(low);
            }

            if (high>idx ) {
                // there are elements in right side to pivot
                visited.push(high);
                visited.push(idx+1);
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