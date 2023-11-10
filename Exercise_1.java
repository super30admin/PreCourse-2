// Time Complexity: O(log n)
// Space Complexity: O(log n)
// Did this code successfully run on Leetcode : yes
// Any problem you faced while coding this : no

/* binary search is performed on below mentioned sorted array
 * use left/right index to calculate mid and compare with x. 
 * if x < array of mid -> a should be on left side 
 * if x > array of mid -> a should be on right side
 * if left and right are equal check if mid value 
 */

class BinarySearch {
	// Returns index of x if it is present in arr[l.. r], else return -1
	int binarySearch(int arr[], int l, int r, int x) {

		while (l <= r) {
			int mid = l + (r - l) / 2;

			if (x == arr[mid]) {
				// mid
				return mid;
			} else if (x < arr[mid]) {
				// left
				return binarySearch(arr, l, mid - 1, x);
			} else if (x > arr[mid]) {
				// right
				return binarySearch(arr, mid + 1, r, x);
			}
		}
		return -1;
	}

	// Driver method to test above
	public static void main(String args[]) {
		BinarySearch ob = new BinarySearch();
		int arr[] = { 0, 1, 3, 4, 10, 40, 50 };
		int n = arr.length;
		int x = 11;
		int result = ob.binarySearch(arr, 0, n - 1, x);
		if (result == -1)
			System.out.println("Element not present");
		else
			System.out.println("Element found at index " + result);
	}
}
