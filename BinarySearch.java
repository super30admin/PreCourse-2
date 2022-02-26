// Time Complexity :  O(logn)   ;where n is the number of elements in the array
// Space Complexity : O(1)

//Code:

class BinarySearch {
    // Returns index of x if it is present in arr[l.. r], else return -1
    int binarySearch(int arr[], int l, int r, int x) {
        // Write your code here
        while (l <= r) {
            int mid = l + (r - l) / 2; // calculating mid value
            if (arr[mid] == x) {
                return mid; // if target value is present at mid index so mid will be returned
            } else if (x < arr[mid]) {
                r = mid - 1; // if mid value is not the target value then we will search by shifting mid to
                             // one left index and one right index and simulateoulsy adjusting the low and
                             // high values
            } else {
                l = mid + 1;
            }
        }
        return -1;
    }

    // Driver method to test above
    public static void main(String args[]) {
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
