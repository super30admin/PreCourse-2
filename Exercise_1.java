// Time Complexity : O(log n)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : No problems faced

// Your code here along with comments explaining your approach

class BinarySearch {
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x)
    {
        //Write your code here
        //loop till low index crosses high index
        while(l <= r) {
            //calculate mid point
            int mid = l + (r - l) / 2;
            //if middle element is equal to search element then return middle index
            if(arr[mid] == x) {
                return mid;
            }
            //if middle element is less than element to search then ignore left half of the array
            if(arr[mid] < x) {
                l = mid + 1;
            } else {
                //middle element is greater than search element
                r = mid - 1;
            }
        }
        //loop exited successfully means element not found
        return -1;
    }

    // Driver method to test above 
    public static void main(String args[])
    {
        BinarySearch ob = new BinarySearch();
        int arr[] = { 2, 3, 4, 10, 40 };
        int n = arr.length;
        int x = 10;
        int result = ob.binarySearch(arr, 0, n - 1, x);
        if (result == -1)
            System.out.println("Element not present");
        else
            System.out.println("Element found at index " + result);
    }
} 
