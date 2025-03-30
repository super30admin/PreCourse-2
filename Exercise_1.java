// Binary Search implementation in Java
// Time Complexity: O(log n)
// Space Complexity: O(1) for iterative, O(log n) for recursive
// This is a recursive implementation of binary search
// It is assumed that the array is sorted in ascending order
// The function returns the index of the element if found, otherwise -1
class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    static int binarySearch(int arr[], int l, int r, int x) { 
        // Base condition
        if (r >= l) {
            int mid = l + (r - l) / 2;

            // Check if the element is present at the middle
            if (arr[mid] == x) {
                return mid;
            }

            // If the element is smaller than mid, search in the left subarray
            if (arr[mid] > x) {
                return binarySearch(arr, l, mid - 1, x);
            }

            // Otherwise, search in the right subarray
            return binarySearch(arr, mid + 1, r, x);
        }

        // Element is not present in the array
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
