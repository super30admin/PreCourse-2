class BinarySearch {
    // Returns index of x if it is present in arr[l.. r], else return -1
    // Space Complexity: O(1)
    // Time Complexity: O(log n)
    int binarySearch(int arr[], int l, int r, int x) {
        // Check left and right pointer.
        // If they have crossed each other -> indicates value not found and stop
        // searching further
        if (l <= r) {
            int midIndex = (l + r) / 2;
            int mid = arr[midIndex];

            if (x == mid) {
                return midIndex;
            } else if (x < mid) {
                // search left side
                return binarySearch(arr, l, midIndex - 1, x);
            } else if (x > mid) {
                // search right side
                return binarySearch(arr, midIndex + 1, r, x);
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
