import java.util.Stack;

class IterativeQuickSort {

    void swap(int arr[], int i, int j)
    {
	//Try swapping without extra variable
        /*
            int a = 10, b = 20;
            a = a + b => a = 30
            b = a - b => b = 30 - 20 => b = 10
            a = a - b => a = 30 - 10 => a = 20
         */

        arr[i] = arr[i] + arr[j];
        arr[j] = arr[i] - arr[j];
        arr[i] = arr[i] - arr[j];
    }

    /* This function is same in both iterative and
       recursive*/
    int partition(int arr[], int low, int high)
    {
        //Compare elements and swap.

        //Write code here for Partition and Swap
        int pivot = arr[high];

        int left = low;
        int right = high -1;
//
//        arr[high] = pivot;

        while(left <= right) {

            if (arr[left] > pivot && arr[right] < pivot) {
                // swap the the left and right elements
                swap(arr, left, right);
                left++;
                right--;
            } else if (arr[left] > pivot) {
                // this mean we are good from the left index point of view
                right--;
            } else {
                // this mean we are good from right index point of view
                left++;
            }
        }


        int pivotIndex = left;
        if(pivotIndex < high && pivotIndex > low)
        swap(arr, pivotIndex, high);

//        System.out.println("Patitioning at index "+ pivotIndex);

        return pivotIndex;
    }

    // Sorts arr[l..h] using iterative QuickSort
    void QuickSort(int arr[], int l, int h)
    {
        //Try using Stack Data Structure to remove recursion.

        int partitionIndex = partition(arr, l, h);

        Stack<Integer> stack = new Stack<>();
        stack.push(partitionIndex);

        while(!stack.isEmpty()){
            int currentIndex = stack.pop();

            System.out.println("Current index "+currentIndex);
            int leftPartition = partition(arr, l, currentIndex -1);
            stack.push(leftPartition);

            int rightPartition = partition(arr, currentIndex + 1, h);
            stack.push(rightPartition);

//            if(currentIndex -1 < h && currentIndex -1 > l) {
//            }
//
//            if(currentIndex + 1 < h && currentIndex + 1 > l) {
//
//            }
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
