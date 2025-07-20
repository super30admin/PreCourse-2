// Time Complexity : O(log n), where n is the number of elements in the array
// Space Complexity : O(1) — because the implementation is iterative and uses no extra space

// Did this code successfully run on Leetcode : Not applicable (custom implementation)

// Any problem you faced while coding this :
// No major issues. Just ensured correct handling of mid-point calculation to avoid overflow.

// Your code here along with comments explaining your approach:
// I implemented an iterative binary search algorithm. Given a sorted array,
// the function repeatedly divides the search range in half.
// It compares the middle element to the target value.
// If the target is smaller, the search continues on the left half;
// if larger, it continues on the right half.
// If the element is found, its index is returned;
// otherwise, the function returns -1.

class BinarySearch {
    // Returns index of x if it is present in arr[l.. r], else return -1 
    // Returns index of x if it is present in arr[l..r], else return -1
    int binarySearch(int arr[], int l, int r, int x) {
        while (l <= r) {
            // Avoids overflow compared to (l + r) / 2
            int mid = l + (r - l) / 2;

            // Check if x is present at mid
            if (arr[mid] == x)
                return mid;

            // If x greater, ignore left half
            if (arr[mid] < x)
                l = mid + 1;

                // If x is smaller, ignore right half
            else
                r = mid - 1;
        }

        // Element not present
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
