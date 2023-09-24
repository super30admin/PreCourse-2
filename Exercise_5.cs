public class IterativeQuickSort
{
    // Time Complexity : O(N log N) - same as recusrive quick sort
    // Space Complexity : O(N) - since we are using stack
    // Did this code successfully run on Leetcode : Yes
    // Any problem you faced while coding this : Yes- understanding the stack concept

    /* This function takes last element as pivot, 
    places the pivot element at its correct 
    position in sorted array, and places all 
    smaller (smaller than pivot) to left of 
    pivot and all greater elements to right 
    of pivot */
    public void swap(int[] arr, int i, int j)
    {
        //Your code here
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    public int partition(int[] arr, int low, int high)
    {
        //Write code here for Partition and Swap 
        int pivot = arr[high];
        int i = low - 1;

        for (int j = low; j < high; j++)
        {
            if (arr[j] < pivot)
            {
                i++;
                swap(arr, i, j);
            }
        }
        swap(arr, i + 1, high);
        return i + 1;
    }

    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    public void QuickSort(int[] arr, int low, int high)
    {
        // Recursively sort elements before 
        // partition and after partition
        int[] stack = new int[high - low + 1];
        int top = -1;

        stack[++top] = low;
        stack[++top] = high;

        while (top >= 0)
        {
            high = stack[top--];
            low = stack[top--];

            int partitionIndex = partition(arr, low, high);

            //left subarray
            if (partitionIndex - 1 > low)
            {
                stack[++top] = low;
                stack[++top] = partitionIndex - 1;
            }

            if (partitionIndex + 1 < high)
            {
                stack[++top] = partitionIndex + 1;
                stack[++top] = high;
            }
        }
    }

    /* A utility function to print array of size n */
    public void printArr(int[] arr, int n)
    {
        int i;
        for (i = 0; i < n; ++i)
            Console.WriteLine(arr[i] + " ");
    }

}
// Driver code to test above 
public static void Main(String[] args)
{
    IterativeQuickSort ob = new IterativeQuickSort();
    int[] arr = { 4, 3, 5, 2, 1, 3, 2, 3 };
    ob.QuickSort(arr, 0, arr.Length - 1);
    ob.printArr(arr, arr.Length);
}
