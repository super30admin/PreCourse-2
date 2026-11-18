// Time: O(log n); Space: O(1)

class BinarySearch {
    // Return the index of x in sorted arr[l..r], or -1 when it is absent.
    int binarySearch(int arr[], int l, int r, int x) {
        while (l <= r) {
            // This form avoids overflowing l + r.
            int mid = l + (r - l) / 2;
            if (arr[mid] == x) {
                return mid;
            }
            if (arr[mid] < x) {
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        return -1;
    }

    public static void main(String args[]) {
        BinarySearch ob = new BinarySearch();
        int arr[] = {2, 3, 4, 10, 40};
        int result = ob.binarySearch(arr, 0, arr.length - 1, 10);
        if (result == -1) {
            System.out.println("Element not present");
        } else {
            System.out.println("Element found at index " + result);
        }
    }
}
