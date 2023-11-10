class BinarySearch {
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int key)
    {
        //Write your code here
        int mid = -1;
        while (l <= r){
             mid = l + ((r - l) / 2);
            if (arr[mid] == key) {
                return mid;
            } else if (arr[mid] < key) {
                l = mid + 1;
            } else if (arr[mid] > key){
                r = mid - 1;
            }
        }
        return mid;
    }

    // Time complexity is O(log n) and best case is O(1)
    // Space complexity is O(1), because it is iterative approach

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