class BinarySearch {

    // Returns index of x if it is present in arr[l.. r], else return -1
    int binarySearch(int arr[], int l, int r, int x) {
        //Write your code here
        int mid = l + r / 2;
        do {
            if (arr[l] == x) {
                return l; /*Comparing lower edge*/
            } else if (arr[r] == x) {
                return r; /*Comparing higher edge*/
            } else if (arr[mid] == x) {
                return mid; /*Comparing Mid*/
            } else if (mid <= r - 1 && arr[mid + 1] == x) {
                return mid + 1; /*Comparing Items next to mid */
            } else if (mid <= r - 1 && mid >=0 && arr[mid - 1] == x) {
                return mid - 1; /*Comparing Items next to mid */
            } else if (arr[mid] < x) {
                l = mid; /*Mid is less than x, need to increment lower limit */
            } else if (arr[mid] > x) {
                r = mid; /*Mid is greater than x, need to decrement higher limit */
            }
            mid = l + r / 2;
         
        } while (l < r);

        return -1;
    }

    // Driver method to test above
    public static void main(String args[]) {
        BinarySearch ob = new BinarySearch();
        int arr[] = {2, 3, 4, 10, 40};
        int n = arr.length;
        int x = 99;

        int result = ob.binarySearch(arr, 0, n - 1, x);
        if (result == -1)
            System.out.println("Element not present");
        else
            System.out.println("Element found at index " + result);
    }
}
