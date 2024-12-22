internal class BinarySearchClass
{

    public int BinarySearch(int[] arr, int l, int r, int x)
    {
        if (l > r)
        {
            return -1;
        }
        var mid = l + (r - l) / 2;
        if (arr[mid] == x) return mid;
        if (arr[mid] < x)
        {
            l = mid + 1;
        }
        else
        {
            r = mid - 1;
        }
        return BinarySearch(arr, l, r, x);
    }
    static void Main(string[] args)
    {
        BinarySearchClass ob = new BinarySearchClass();
        int[] arr = { 2, 3, 4, 10, 40 };
        int n = arr.Length;
        int x = 0;
        int result = ob.BinarySearch(arr, 0, n - 1, x);
        if (result == -1)
        {
            Console.WriteLine("Element not present");
        }
        else
        {
            Console.WriteLine("Element found at index " + result);
        }
    }

}