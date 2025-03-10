// Time Complexity :O(logn)
// Space Complexity :O(1)
// Did this code successfully run on Leetcode :Yes
// Any problem you faced while coding this :No


class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        // run the loop till left index is smaller or equal to right index
    while (l <= r) {
        // finding the middle index
        int mid = l + (r - l) / 2;

        // check if mid element is equal to the target
        if (arr[mid] == x) {
            return mid;
        }
        // if x is smaller, search left half
        if (arr[mid] > x) {
            r = mid - 1;
        }
        // if x is greater, search right half
        else {
            l = mid + 1;
        }
    }
    // if element not found
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
