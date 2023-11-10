// Time Complexity : O(log n)
// Space Complexity : O(n)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : No

class BinarySearch {
    // Returns index of x if it is present in arr[l.. r], else return -1
    int binarySearch(int arr[], int l, int r, int x)
    {
        // If element is present in the array
        if (r >= l) {
            // find the mid point
            int mid = l + (r - l) / 2;
            if(x == arr[mid]){ //if the element we are looking for is the mid point
                return mid;
            }
            if(x < arr[mid]){ // if the element is less than the mid point
                return binarySearch(arr, l, mid - 1, x);
            }
            // if the element is greater than the mid point
            return binarySearch(arr, mid+1, r, x);
        }
        // return -1 if element is not found
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
