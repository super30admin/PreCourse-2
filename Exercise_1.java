// Time Complexity : O(logn)
// during each iteration inside the while loop, your search space is halved. 

// Space Complexity : O(1) as we are not using any additional space 

class BinarySearch {
    // Returns index of x if it is present in arr[l.. r], else return -1
    int binarySearch(int arr[], int l, int r, int x) {
        // checking whether the input array is null or empty
        if (arr == null || arr.length == 0)
            return -1;

        while (l <= r) {
            int mid = l + (r - l) / 2; // calculating mid index like this helps you avoid integer overflow situation
            if (arr[mid] == x)
                return mid;
            else if (arr[mid] > x)
                r = mid - 1;
            else
                l = mid + 1;
        }
        return -1;
    }
}

class Exercise_1 {
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
