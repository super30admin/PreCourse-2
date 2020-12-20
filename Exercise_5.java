import java.util.Stack;

/*
instead of using inbuilt recursion stack, we create own stack DS to store the indices of left and right boundaries
of sub array.

 */
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

    //partition function remains same for recursive and iterative algorithm

    int partition(int arr[], int low, int high)
    {
        //Compare elements and swap.
        int pivot = arr[high]; // assigning  the right most element as pivot
        int index = (low-1);
        for (int j = low; j < high;j++){
            if (arr[j] <= pivot){
                index++;
                swap(arr,index,j);
            }
        }
        swap(arr,index+1,high);
        return index+1;
    }

    // Sorts arr[l..h] using iterative QuickSort
    void QuickSort(int arr[], int low, int high)
    {
        //Try using Stack Data Structure to remove recursion.
        Stack<Integer> stack  = new Stack<>();
        stack.push(low);
        stack.push(high);
        while (!stack.isEmpty()){
            int right = stack.pop();
            int left = stack.pop();

            int p = partition(arr,left,right);
            //pushing indices of subarray to the left side of pivot index
            if (p-1 > left){
                stack.push(left);
                stack.push(p-1);
            }
            //pushing indices of subarray to the right side of pivot index
            if (p+1 < right){
                stack.push(p+1);
                stack.push(right);
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