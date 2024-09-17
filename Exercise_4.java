// Time Complexity : O(nlogn)
// Space Complexity : O(n) 
// Did this code successfully run on Leetcode : 
// Any problem you faced while coding this : No

public class Exercise_4 {
	// Merges two subarrays of arr[].
	// First subarray is arr[l..m]
	// Second subarray is arr[m+1..r]
	void merge(int arr[], int l, int m, int r) {
		int n1 = m - l + 1;
		int n2 = r - m;

		int[] leftArr = new int[n1];
		int[] rightArr = new int[n2];

		for (int i = 0; i < n1; i++) {
			leftArr[i] = arr[l + i];
		}
		for (int j = 0; j < n2; j++) {
			rightArr[j] = arr[m + 1 + j];
		}

		int i = 0, j = 0;
		int k = l;

		while (i < n1 && j < n2) {
			if (leftArr[i] <= rightArr[j]) {
				arr[k] = leftArr[i];
				i++;
			} else {
				arr[k] = rightArr[j];
				j++;
			}
			k++;
		}

		while (i < n1) {
			arr[k++] = leftArr[i++];
		}

		while (j < n2) {
			arr[k++] = rightArr[j++];
		}

	}

	// Main function that sorts arr[l..r] using
	void sort(int arr[], int l, int r) {
		// Recursively sort the 2 divided arrays and merge them.
		if (l < r) {
			int middle = l + (r - l) / 2;
			sort(arr, l, middle);
			sort(arr, middle + 1, r);
			merge(arr, l, middle, r);
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

		Exercise_4 ob = new Exercise_4();
		ob.sort(arr, 0, arr.length - 1);

		System.out.println("\nSorted array");
		printArray(arr);
	}
}