class MergeSort {
	// Merges two subarrays of arr[].
	// First subarray is arr[l..m]
	// Second subarray is arr[m+1..r]
	void merge(int arr[], int l, int m, int r) {
		int tempd[] = new int[r - l + 1];
		int i = 0;
		int k = m + 1;
		int lOrig = l;
		while (k <= r && l <=m) {
			if (arr[l] < arr[k]) {
				tempd[i] = arr[l];
				l++;
			} else {
				tempd[i] = arr[k];
				k++;
			}
			i++;
		}
		while (l <= m) {
			tempd[i] = arr[l];
			l++;
			i++;
		}
		while (k <= r) {
			tempd[i] = arr[k];
			k++;
			i++;
		}
		k = 0;
		for (i = lOrig; i <= r; i++) {
			arr[i] = tempd[k];
			k++;
		}
	}

	// Main function that sorts arr[l..r] using
	// merge()
	void sort(int arr[], int l, int r) {
		// Write your code here
		// Call mergeSort from here
		if (l == r)
			return;
		int m = (l + r) / 2;
		sort(arr, l, m);
		sort(arr, m + 1, r);
		merge(arr, l, m, r);
	}

	/* A utility function to print array of size n */
	static void printArray(int arr[]) {
		
		int n = arr.length;
		for (int i = 0; i < n; ++i)
			System.out.print(arr[i] + " ");
		System.out.println();
	}

	// Driver method
	public static void main(String args[]) {
		int arr[] = { 12, 11, 13, 5, -1, -6, 8, 9};
		System.out.println("Given Array");
		printArray(arr);

		MergeSort ob = new MergeSort();
		ob.sort(arr,0, arr.length - 1);

		System.out.println("\nSorted array");
		printArray(arr);
	}
}