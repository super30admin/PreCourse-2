// Time Complexity : O(logN)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode :
// Any problem you faced while coding this :
// Time Complexity : O(logN)
// Space Complexity : 0(1)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : yes, i had used the comparison  l <r where the check for the last element was failing
// I had also used the condition on line 24 and 26 as l = mid and r = mid and this was leading to finite looping due to assingment
// and eventually the code timed out.

class BinarySearch {
    // Returns index of x if it is present in arr[l.. r], else return -1
    int binarySearch(int arr[], int l, int r, int x)
    {
        //Write your code here
        if (arr.length == 0) {
            return -1;
        }
        int mid = (l + r) / 2;
        while (l <= r) {
            if (arr[mid] == x ) {
                return mid;
            } else if ( x > arr[mid]) {
                l = mid + 1;
            } else if (x < arr[mid]) {
                r = mid - 1 ;
            }
            mid = (l + r) / 2;
        }
        return -1;
    }

    // Driver method to test above
    public static void main(String args[])
    {
        BinarySearch ob = new BinarySearch();
        int arr[] = { 2, 3, 4, 10, 40 };
        int n = arr.length;
        int result;
        result = ob.binarySearch(arr, 0, n - 1, 10);
        if (result == -1)
            System.out.println("Element not present");
        else
            System.out.println("Element found at index " + result);
        //Check if first element's index is returned successfully
        result = ob.binarySearch(arr, 0, n - 1, 2);
        if (result == -1)
            System.out.println("Element not present");
        else
            System.out.println("Element found at index " + result);
        // Check if last element's index is returned successfully
        result = ob.binarySearch(arr, 0, n - 1, 40);
        System.out.println("Last Element result:" + result);
        if (result == -1)
            System.out.println("Element not present");
        else
            System.out.println("Element found at index " + result);
        // Check if search for missing element returns -1 and prints the reason
        result = ob.binarySearch(arr, 0, n - 1, 100);
        if (result == -1)
            System.out.println("Element not present");
        else
            System.out.println("Element found at index " + result);
    }
}
