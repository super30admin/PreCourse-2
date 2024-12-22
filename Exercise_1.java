//TC: O(log(n)) where n is size of array
//SC: O(n) where n is size of array, to store the array

class BinarySearch {
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) {
        if (l == r) {
            return (arr[l] == x) ? l : -1;
        }
        if (l == r - 1) {
            if (x != arr[l] && x != arr[r]) return -1;
            return x == arr[l] ? l : r;
        }
        int mid = l + ((r - l) / 2);
        if (x == arr[mid]) return mid;
        else if (x > arr[mid]) {
            return binarySearch(arr, mid, r, x);
        } else return binarySearch(arr, l, mid, x);

    }

    // Driver method to test above 
    public static void main(String args[]) {
        BinarySearch ob = new BinarySearch();
        int arr[] = {2, 3, 4, 10, 40};
        int n = arr.length;
        int x = 10;
        int result = ob.binarySearch(arr, 0, n - 1, x);
        if (result == -1)
            System.out.println("Element not present");
        else
            System.out.println("Element found at index " + result);
    }
} 
