// Time Complexity : O(nLogn)
// Space Complexity : O(n)
// Did this code successfully run on Leetcode : yes
// Any problem you faced while coding this : no

// Your code here along with comments explaining your approach
// The array is divided into 2 parts recursively until single value array. merge all values at the end to form sorted array.
class MergeSort {
	// Merges two subarrays of arr[].
	// First subarray is arr[l..m]
	// Second subarray is arr[m+1..r]
	void merge(int arr[], int l, int m, int r) {
		// Your code here
		int len1 = m - l + 1;
		int len2 = r - m;

		int[] arr1 = new int[len1];
		int[] arr2 = new int[len2];

		for (int i = 0; i < len1; ++i)
			arr1[i] = arr[i + l];
		for (int i = 0; i < len2; ++i)
			arr2[i] = arr[i + m + 1];

		int i = 0;
		int j = 0;
		int k = l;

		while (i < len1 && j < len2) {
			if (arr1[i] <= arr2[j])
				arr[k++] = arr1[i++];
			else
				arr[k++] = arr2[j++];
		}

		while (i < len1)
			arr[k++] = arr1[i++];
		while (j < len2)
			arr[k++] = arr2[j++];
	}

	// Main function that sorts arr[l..r] using
	// merge()
	void sort(int arr[], int l, int r) {
		// Write your code here
		// Call mergeSort from here
		if (l < r) {
			int mid = l + (r - l) / 2;

			sort(arr, l, mid);
			sort(arr, mid + 1, r);

			merge(arr, l, mid, r);
		}

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
		int arr[] = { 12, 11, 13, 5, 6, 7 };

		System.out.println("Given Array");
		printArray(arr);

		MergeSort ob = new MergeSort();
		ob.sort(arr, 0, arr.length - 1);

		System.out.println("\nSorted array");
		printArray(arr);
	}
}