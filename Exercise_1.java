// Time Complexity : O(logn)
// Space Complexity : O(1)
class BinarySearch {
    // Returns index of x if it is present in arr[l.. r], else return -1
    static int binarySearch(int arr[], int l, int r, int x) {
        int left = l, right = r, mid = 0;
        if (arr == null || arr.length == 0) {
            return -1;
        } else {
            while (left <= right) {
                // calculating mid
                mid = (left + right) / 2;
                // x if at mid index
                if (x == arr[mid]) {
                    return mid;
                }
                // if x is smaller than mid,it must be in left half
                else if (x <= arr[mid]) {
                    right = mid - 1;
                }
                // if x is smaller than mid,it must be in left half)
                else if (x > arr[mid]) {
                    left = mid + 1;
                }
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
