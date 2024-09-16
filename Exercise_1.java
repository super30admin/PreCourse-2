/*
   Binary Search
	1)Time Complexity: O(logN)
	2)Space Complexity: O(1)
	3)Was able to run successfully on leetcode
	4)No Problem faced during coding the problem 
*/

class BinarySearch {
	// Returns index of x if it is present in arr[l.. r], else return -1
	int binarySearch(int arr[], int l, int r, int x) {
		// Write your code here

		// Terminating condition
		if (r >= l) {
			/*
			 * We use this to prevent Overflow and to find the middle index of the first and
			 * last index
			 */
			int middle = l + (r - l) / 2;
			/*
			 * if the middle index of the array is equal to element we return the middle
			 * index
			 */
			if (arr[middle] == x) {
				return middle;
			}
			/*
			 * If the middle index is greater than the element to be searched we perform
			 * recursion until the terminating condition is reached and decrement last index
			 * to middle-1
			 */
			if (arr[middle] > x) {
				return binarySearch(arr, l, middle - 1, x);
			}
			/*
			 * If the middle index is less than the element to be searched we perform
			 * recursion until the terminating condition is reached and increment the first
			 * index to middle+1
			 */
			else {
				return binarySearch(arr, middle + 1, r, x);
			}
		}
		// return -1, if the element is not present
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
