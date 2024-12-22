internal class Program
{
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    static void Merge(int[] arr, int l, int m, int r)
    {
        var leftLength = m - l + 1;
        var rightLength = r - m;

        var leftArray = new int[leftLength];
        var rightArray = new int[rightLength];

        for (var i = 0; i < leftLength; i++)
        {
            leftArray[i] = arr[l + i];
        }
        for (var j = 0; j < rightLength; j++)
        {
            rightArray[j] = arr[m + 1 + j];
        }

        var iIndex = 0;
        var jIndex = 0;
        var k = l;

        while (iIndex < leftLength && jIndex < rightLength)
        {
            if (leftArray[iIndex] <= rightArray[jIndex])
            {
                arr[k] = leftArray[iIndex];
                iIndex++;
            }
            else
            {
                arr[k] = rightArray[jIndex];
                jIndex++;
            }
            k++;
        }

        while (iIndex < leftLength)
        {
            arr[k] = leftArray[iIndex];
            iIndex++;
            k++;
        }

        while (jIndex < rightLength)
        {
            arr[k] = rightArray[jIndex];
            jIndex++;
            k++;
        }

    }

    // Main function that sorts arr[l..r] using 
    // merge() 
    static void Sort(int[] arr, int l, int r)
    {
        if (l >= r) return;

        var m = l + (r - l) / 2;

        Sort(arr, l, m);
        Sort(arr, m + 1, r);

        Merge(arr, l, m, r);
    }

    /* A utility function to print array of size n */
    static void PrintArray(int[] arr)
    {
        int n = arr.Length;
        for (int i = 0; i < n; ++i)
        {
            System.Console.WriteLine(arr[i] + " ");
        }
        Console.WriteLine();
    }
    static void Main(string[] args)
    {
        int[] arr = { 12, 11, 13, 5, 6, 7 };

        Console.WriteLine("Given Array");
        PrintArray(arr);

        Sort(arr, 0, arr.Length - 1);

        Console.WriteLine("\nSorted array");
        PrintArray(arr);
        Console.ReadKey();
    }
}