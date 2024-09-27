/*Time Complexity : O(log N) N is constant here, N=5
 Space Complexity : O(1), no additional space used


 Your code here along with comments explaining your approach: I would divide the array in half by calculating mid value.
 Compare the target with mid value, if target is less than mid, I will search in left half(lower) of the mid index.
 If target is greater than mid value, I will search in right half(upper) of the mid index.
 If value is equal to the value at mid return mid index else return -1;
*/
class BinarySearch {
    // Returns index of x if it is present in arr[l.. r], else return -1
    int binarySearch(int arr[], int l, int r, int x) {
        // Sort the array if array is not sorted
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (arr[mid] == x) {
                return mid;
            } else if (arr[mid] < x) {
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        return -1;
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
