class BinarySearch {
	// Returns index of x if it is present in arr[l.. r], else return -1
	int binarySearch(int arr[], int l, int r, int x) {
		int m = (l + r) / 2;
		if (x == arr[m])
			return m;
		if (l == r)
			return -1;

		if (x < arr[m])
			return binarySearch(arr, l, m, x);
		else
			return binarySearch(arr, m + 1, r, x);

	}

	// Driver method to test above
	public static void main(String args[]) {
		BinarySearch ob = new BinarySearch();
		int arr[] = { 2, 3, 4, 10, 40, 60, 70 };
		int n = arr.length;
		int x = 0;
		int result = ob.binarySearch(arr, 0, n - 1, x);
		if (result == -1)
			System.out.println("Element not present");
		else
			System.out.println("Element found at index " + result);
	}
}
