// Time Complexity : O(log n) if the array is sorted
// Space Complexity : O(1) -> Not using any extra space 
// Did this code successfully run on Leetcode : 
// Any problem you faced while coding this : No

public class Exercise_1 {
	// Returns index of x if it is present in arr[l.. r], else return -1
	int binarySearch(int arr[], int l, int r, int x) {
		if (arr.length == 0) {
			return -1;
		}

		while (l <= r) {
			// Get the middle element of the array. If the element is the target, return x
			// If not, discard one half of the array, and follow the above step on the other half
			int m = l + (r - l) / 2;
			if (arr[m] == x) {
				return m;
			} else if (arr[m] < x) {
				l = m + 1;
			} else {
				r = m - 1;
			}
		}
		return -1;
	}

	// Driver method to test above
	public static void main(String args[]) {
		Exercise_1 ob = new Exercise_1();
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
