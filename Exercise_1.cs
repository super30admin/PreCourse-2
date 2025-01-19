// Time Complexity :O(logN) where N = number of elements in array
// Space Complexity : O(1) 
using System;

class BinarySearch
{
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int[] arr, int l, int r, int x)
    {
        //Write your code here
        while (l <= r)
        {
            int mid = (l + r) / 2;
            if (arr[mid] == x)
            {
                return mid;
            }
            if (x >= arr[l] && x < arr[mid])
            {
                r = mid - 1;
            }
            else
            {
                l = mid + 1;
            }

        }
        return - 1;
    }

    // Driver method to test above 
    public static void Main(string[] args)
    {
        BinarySearch ob = new BinarySearch();
        int[] arr = { 2, 3, 4, 10, 40 };
        int n = arr.Length;
        int x = 10;
        int result = ob.binarySearch(arr, 0, n - 1, x);
        if (result == -1)
            Console.WriteLine("Element not present");
        else
            Console.WriteLine("Element found at index " + result);
        Console.ReadLine();
    }
}