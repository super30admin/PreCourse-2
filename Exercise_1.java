// Time Complexity is O(logN)
// Space Complexity is O(1)

class BinarySearch {

    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) {
        //Write your code here
        // iterating through array
        while (l <= r) {
            int mid = (l + r) / 2;

            // checking if mid is target or not
            if (arr[mid] == x) {
                return mid;
            } //checking if target is in the first half or second half
            else if (x > arr[mid]) {
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }

        // if target not found
        return -1;

    }

    // Driver method to test above 
    public static void main(String args[]) {
        BinarySearch ob = new BinarySearch();
        int arr[] = {2, 3, 4, 10, 40};
        int n = arr.length;
        int x = 10;
        int result = ob.binarySearch(arr, 0, n - 1, x);
        if (result == -1) {
            System.out.println("Element not present"); 
        }else {
            System.out.println("Element found at index " + result);
        }
    }
}
