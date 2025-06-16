// Time Complexity:
// O(log n) - In each step, the search space is divided by 2

// Space Complexity:
// O(1)

class BinarySearch {
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    {
        while (l <= r) {
            int mid = l + (r - l) / 2;

            // Check if x is present at mid
            if (arr[mid] == x)
                return mid;

            // If x is smaller, ignore the right half
            if (arr[mid] > x)
                r = mid - 1;

                // If x is larger, ignore the left half
            else
                l = mid + 1;
        }

        // Element is not present in array
        return -1;
    }

    // Driver method to test above 
    public static void main(String args[]) 
    { 
        BinarySearch ob = new BinarySearch(); 
        int[] arr = { 2, 3, 4, 10, 40 };
        int n = arr.length; 
        int x = 10; 
        int result = ob.binarySearch(arr, 0, n - 1, x); 
        if (result == -1) 
            System.out.println("Element not present"); 
        else
            System.out.println("Element found at index " + result); 
    } 
} 
