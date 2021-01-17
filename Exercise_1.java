// T:O(logn) S:O(1)
class BinarySearch {
    // Returns index of x if it is present in arr[l.. r], else return -1
    int binarySearch(int arr[], int l, int r, int x) {
        // Write your code here
        int index = (r + 1) / 2, i = 0, j = r;

        while (i <= j) {
            if (arr[index] == x)
                return index;
            else if (arr[index] < x) {
                i = index + 1;
                index = i + (j - i) / 2;
            } else {
                j = index - 1;
                index = i + (j - i) / 2;
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
