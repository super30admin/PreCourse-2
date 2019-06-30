class BinarySearch {
	// Returns index of x if it is present in arr[l.. r], else return -1
	int binarySearch(int arr[], int l, int r, int x) {
		// Write your code here
		if (r > 0) {							// till right is greater than 0
			int m = l + (r - l) / 2;			// find mid value

			if (arr[m] == x) {					// if x is mid value, return mid value
				return m;
			}

			if (arr[m] > x) {					// if x falls on the left side of mid value, recurse thru binary search 
				binarySearch(arr, l, m - 1, x);	// method, keeping right value as mid-1.
			} else
				binarySearch(arr, m + 1, r, x);	// else recurse keeping low/left value as mid+1
		}
		return -1;								// number is not found
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
