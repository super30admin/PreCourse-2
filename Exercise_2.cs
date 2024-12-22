class QuickSort
{
    /* This function takes last element as pivot, 
places the pivot element at its correct 
position in sorted array, and places all 
smaller (smaller than pivot) to left of 
pivot and all greater elements to right 
of pivot */
    static void Swap(int[] arr, int i, int j)
    {
        var temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    static int Partition(int[] arr, int low, int high)
    {
        var pivot = arr[high];
        var swapIndex = low - 1;

        for (var i = low; i <= high; i++)
        {
            if (arr[i] <= pivot)
            {
                swapIndex++;
                Swap(arr, i, swapIndex);
            }
        }
        return swapIndex;
    }
    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    static void Sort(int[] arr, int low, int high)
    {
        if (low > high) return;
        var pivot = Partition(arr, low, high);
        Sort(arr, low, pivot - 1);
        Sort(arr, pivot + 1, high);
    }

    /* A utility function to print array of size n */
    static void PrintArray(int[] arr)
    {
        int n = arr.Length;
        for (int i = 0; i < n; ++i)
        {
            Console.WriteLine(arr[i]);
        }
        Console.WriteLine();
    }

    // Driver program 
    static void Main(string[] args)
    {
        int[] arr = { 10, 7, 8, 9, 1, 5 };
        int n = arr.Length;

        //QuickSort ob = new QuickSort();
        Sort(arr, 0, n - 1);

        Console.WriteLine("sorted array");
        PrintArray(arr);
    }
}