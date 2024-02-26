/**
 * Implements Binary Search Algorithm
 * @author Prajwal Chinchmalatpure
 * Time complexity: O(log n) without input validation. O(n) with input validation
 * Space complexity: O(1) for iterative O(logn) for recursive,
 * where n is the number of elements in the array
 */
class BinarySearch {

    /**
     * Returns index of x if it is present in arr[l.. r], else return -1
     * @param arr input array which is not always sorted
     * @param l left index value of array or sub array
     * @param r right index value of array or sub array
     * @param x target element
     * @return index of target
     */
    int binarySearchIterative(int[] arr, int l, int r, int x)
    {
        // Input validation
        if (l > r || r >= arr.length || l < 0) {
            System.out.println("Invalid input");
            return -1;
        }

        // Check if array is sorted
        for (int i = 0; i < arr.length - 1; i++) {
            if (arr[i] > arr[i + 1]) {
                System.out.println("Array is not sorted");
                return -1;
            }
        }

        int midIndex;
        while (l <= r) {
            midIndex = l + (r - l) / 2;
            if (arr[midIndex] == x) {
                return midIndex;
            }
            else if (arr[midIndex] > x) { // Explore left half on input array
                r = midIndex - 1;
            }
            else {
                l = midIndex + 1; //Explore right side of the array
            }
        }

        // If x is not found, we return -1
        return -1;
    }

    // This has better readability but worse space complexity
    int binarySearchRecursive(int[] arr, int l, int r, int x) {
        // Input validation
        if (l > r || r >= arr.length || l < 0) {
            System.out.println("Invalid input or target element not present");
            return -1;
        }

        // Check if array is sorted
        for (int i = 0; i < arr.length - 1; i++) {
            if (arr[i] > arr[i + 1]) {
                System.out.println("Array is not sorted");
                return -1;
            }
        }
        int midIndex = l + (r - l) / 2;
        if (arr[midIndex] == x) {
            return midIndex;
        }
        else if (arr[midIndex] > x) {
            binarySearchRecursive(arr, l, midIndex - 1, x); // Recursive call for left half
        }
        else {
            binarySearchRecursive(arr, midIndex + 1, r, x); // Recursive call for right half
        }
        return -1; // If element not present in array
    }
  
    // Driver method to test above 
    public static void main(String args[]) 
    { 
        BinarySearch ob = new BinarySearch(); 
        int arr[] = { 2, 3, 4, 10, 40 }; 
        int n = arr.length; 
        int x = 10; 
        int result = ob.binarySearchIterative(arr, 0, n - 1, x);
        System.out.println("Recursive implementation result: " + ob.binarySearchRecursive(arr, 0, n - 1, x));
        if (result == -1) 
            System.out.println("Element not present"); 
        else
            System.out.println("Element found at index " + result);
    } 
} 
