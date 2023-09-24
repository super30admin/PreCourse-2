public class QuickSort
{
    // Time Complexity : O(N log N)
    // Space Complexity : O(1)
    // Did this code successfully run on Leetcode : Yes
    // Any problem you faced while coding this : No

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
    public void sort(int[] arr, int low, int high)
    {
        // Recursively sort elements before 
        // partition and after partition
        if (low < high)
        {
            int partitionIndex = partition(arr, low, high);

            sort(arr, low, partitionIndex - 1);
            sort(arr, partitionIndex + 1, high);
        }
    }

    /* A utility function to print array of size n */
    public void printArray(int[] arr)
    {
        int n = arr.Length;
        for (int i = 0; i < n; ++i)
            Console.WriteLine(arr[i] + " ");
        Console.WriteLine();
    }

}

// Driver program 
public static void Main(String[] args)
{
    int[] arr = { 10, 7, 8, 9, 1, 5 };
    int n = arr.Length;

    QuickSort ob = new QuickSort();
    ob.sort(arr, 0, n - 1);

    Console.WriteLine("sorted array");
    ob.printArray(arr);
}
