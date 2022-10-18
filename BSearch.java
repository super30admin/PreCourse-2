///Time and space complexity
//Time Complexity: O(log n)
//Space Complexity: O(1)
package Precourse2;
public class BSearch {
	int binarySearch(int arr[], int x)
    {
        int l = 0, r = arr.length - 1;
        while (l <= r) {
            int m = l + (r - l) / 2;
            if (arr[m] == x)
                return m;
            if (arr[m] < x)
                l = m + 1;
            else
                r = m - 1;
        }
        return 0;
    }
    public static void main(String args[])
    {
        BSearch ob = new BSearch();
        int arr[] = { 2, 3, 4, 10, 40 };
        int x = 10;
        int result = ob.binarySearch(arr, x);
        if (result == 0)
            System.out.println("Element not present");
        else
            System.out.println("Element found at "
                               + "index " + result);
    }
}
