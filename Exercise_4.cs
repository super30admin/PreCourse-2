//Time Complexity = O(nlogn)
//Space Complexity = O(n)
class MergeSort
{
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int[] arr, int l, int m, int r)
    {
        //Your code here  
        int n1 = m - l + 1;
        int n2 = r - m;

        int[] left = new int[n1];
        int[] right = new int[n2];

        for (int i = 0; i < n1; i++)
            left[i] = arr[l + i];

        for (int j = 0; j < n2; j++)
            right[j] = arr[m + 1 + j];

        int iIndex = 0, jIndex = 0, k = l;

        while (iIndex < n1 && jIndex < n2)
        {
            if (left[iIndex] <= right[jIndex])
                arr[k++] = left[iIndex++];
            else
                arr[k++] = right[jIndex++];
        }

        while (iIndex < n1)
            arr[k++] = left[iIndex++];

        while (jIndex < n2)
            arr[k++] = right[jIndex++];
    }

    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int[] arr, int l, int r)
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

    //int[] arr = {12, 11, 13, 5, 6, 7}; 
    /* A utility function to print array of size n */
    static void printArray(int[] arr)
    {
        int n = arr.length;
        for (int i = 0; i < n; ++i)
            Console.WriteLine(arr[i] + " ");
        Console.ReadLine();
    }

    // Driver method 
    public static void main(String[] args)
    {
        int[] arr = { 12, 11, 13, 5, 6, 7 };

        Console.WriteLine("Given Array");
        printArray(arr);

        MergeSort ob = new MergeSort();
        ob.sort(arr, 0, arr.length - 1);

        Console.WriteLine("\nSorted array");
        printArray(arr);
    }
} 