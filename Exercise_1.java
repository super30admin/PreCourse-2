// Time Complexity : O(Log n)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : Tested successfully on local code editor.
// Any problem you faced while coding this : No

//Approach: I have used two variables low, high that marks the start and end of the search space. mid is element at the middle of the search space.
//If mid == x, return mid+1 as the position where x id found. Else modify the start or end of the search space depending on whether x is less than mid,
//search in the left half by making high as mid-1
//or if x is greater than mid, search in the right half by making low to be mid+1.
//in the end if x is not found return -1.

class BinarySearch {
    // Returns index of x if it is present in arr[l.. r], else return -1
    int binarySearch(int arr[], int l, int r, int x)
    {
        //Write your code here
        int low = l;
        int high = r;
        while(low <= high) {
            int mid = low + (high-low)/2;
            if(arr[mid] == x) {
                return mid+1;
            } else if (arr[mid] > x) {
                high = mid-1;
            } else {
                low = mid+1;
            }
        }
        return -1;
    }

    // Driver method to test above
    public static void main(String args[])
    {
        BinarySearch ob = new BinarySearch();
        int arr[] = { 2, 3, 4, 10, 40 };
        int n = arr.length;
        int x = 7;
        int result = ob.binarySearch(arr, 0, n - 1, x);
        if (result == -1)
            System.out.println("Element not present");
        else
            System.out.println("Element found at index " + result);
    }
}
