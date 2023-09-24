public class BinarySearch
{
    // Time Complexity : O(log N)
    // Space Complexity : O(log N)
    // Did this code successfully run on Leetcode : Yes
    // Any problem you faced while coding this : No
    public int binarySearch(int[] arr, int l, int r, int x)
    {
        //Write your code here
        if (r >= l)
        {
            int mid = l + (r - l) / 2;
            if (arr[mid] == x)
                return mid;
            if (arr[mid] < x) //moving right
                return binarySearch(arr, mid + 1, r, x);
            if (arr[mid] > x) // moving left
                return binarySearch(arr, l, mid - 1, x);
        }
        return -1;
    }

}

// Driver method to test above 
public static void Main(String[] args)
{
    BinarySearch ob = new BinarySearch();
    int[] arr = { 2, 3, 4, 10, 40 };
    int n = arr.Length;
    int x = 4;
    int result = ob.binarySearch(arr, 0, n - 1, x);
    if (result == -1)
        Console.WriteLine("Element not present");
    else
        Console.WriteLine("Element found at index " + result);
}
