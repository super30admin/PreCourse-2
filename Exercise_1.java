ackage s30.preCourse2;

class BinarySearch {
    // Returns index of x if it is present in arr[l.. r], else return -1
    int binarySearch(int arr[], int l, int r, int x)
    {
        if(r >= l) {
            int mid = (l + r) / 2;
            if (arr[mid] == x) return x;
            if (x < arr[mid]) return binarySearch(arr, l, mid - 1, x);
            else return binarySearch(arr, mid + 1, r, x);
        }
        return -1;
    }

    //h = 10 & l = 6
    //h = 6 + 10-6/2
    int binarySearchIterative(int arr[], int l, int r, int x)
    {
        while(l <= r) {
            int mid = l + (r-l)/2;
            if(arr[mid] == x) {
                return x;
            }
            if (arr[mid] < x) {
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }
        return -1;
    }

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
