class BinarySearch {
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x)
    {

        if (l <= r) {
            int mid = (l+r)/2;
            System.out.println(mid);
            System.out.println(arr[mid]);
            System.out.println(x);
            if (x == arr[mid]) {
                return mid;
            }
            if (x < arr[mid]) {
                return binarySearch(arr, l, mid - 1, x);
            }
            if (x > arr[mid]) {
                return binarySearch(arr, mid + 1, r, x);
            }
        }
        return -1;
    }

    // Driver method to test above 
    public static void main(String args[])
    {
        BinarySearch ob = new BinarySearch();
        int arr[] = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};
        int n = arr.length;
        int x = 91;
        int result = ob.binarySearch(arr, 0, n - 1, x);
        if (result == -1)
            System.out.println("Element not present");
        else
            System.out.println("Element found at index " + result);
    }
}
