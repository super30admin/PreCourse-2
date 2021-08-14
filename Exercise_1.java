class BinarySearch
{

    // Returns index of x if it is present in arr[l.. r], else return -1
    int binarySearch(int arr[], int l, int r, int x)
    {
        //Write your code here
        while (l <= r)
        {
            int m = l + (r - l) / 2;
            if (arr[m] == x)
            {
                return m;
            }
            if (arr[m] < x)
            {
                l = m + 1;
            }
            if (arr[m] > x)
            {
                r = m - 1;
            }
        }
        return -1;
    }

    // Driver method to test above
    public static void main(String args[])
    {
        BinarySearch ob = new BinarySearch();
        int arr[] = {2, 3, 4, 10, 40};
        int n = arr.length;
        int x = 3;
        int result = ob.binarySearch(arr, 0, n - 1, x);
        if (result == -1)
            System.out.println("Element not present");
        else
            System.out.println("Element found at index " + result);
    }
}
/*
// Time Complexity : log(n) where n is the size of an array
// Space Complexity : O(1) constant space
// Did this code successfully run on Leetcode : I didn't ran on Leetcode
// Any problem you faced while coding this : Overflow error during calculating middle element
Earlier, I had written int m = (r-l)/2. It was giving me overflow exception.

 */