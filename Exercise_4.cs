public class MergeSort
{

    // Time Complexity : O(N log N) - recursive algorithm
    // Space Complexity : O(N) - since we are using additional array
    // Did this code successfully run on Leetcode : Yes
    // Any problem you faced while coding this : Yes - needed more time to understand the merge process

    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    public void merge(int[] arr, int l, int m, int r)
    {
        //Your code here

        int leftArrSize = m - l + 1;
        int rightArrSize = r - m;

        int[] leftArr = new int[leftArrSize];
        int[] rightArr = new int[rightArrSize];

        int i;
        int j;

        for (i = 0; i < leftArrSize; ++i)
        {
            leftArr[i] = arr[l + i];
        }

        for (j = 0; j < rightArrSize; ++j)
        {
            rightArr[j] = arr[m + 1 + j];
        }

        i = 0; //left array
        j = 0; //right array

        int k = l;

        while (i < leftArrSize && j < rightArrSize)
        {
            if (leftArr[i] <= rightArr[j])
            {
                arr[k] = leftArr[i];
                i++;
            }
            else
            {
                arr[k] = rightArr[j];
                j++;
            }
            k++;
        }

        while (i < leftArrSize)
        {
            arr[k] = leftArr[i];
            i++;
            k++;
        }

        while (j < rightArrSize)
        {
            arr[k] = rightArr[j];
            j++;
            k++;
        }
    }

    // Main function that sorts arr[l..r] using 
    // merge() 
    public void sort(int[] arr, int l, int r)
    {
        //Write your code here
        //Call mergeSort from here 
        if (l < r)
        {
            int m = l + (r - l) / 2;

            sort(arr, l, m);
            sort(arr, m + 1, r);

            merge(arr, l, m, r);
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

// Driver method 
public static void Main(String[] args)
{
    MergeSort ob = new MergeSort();
    int[] arr = { 12, 11, 13, 5, 6, 7 };

    Console.WriteLine("Given Array");
    ob.printArray(arr);


    ob.sort(arr, 0, arr.Length - 1);

    Console.WriteLine("\nSorted array");
    ob.printArray(arr);
}
