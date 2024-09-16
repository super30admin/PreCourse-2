/*
   Merge Sort
	1)Time Complexity: O(NLogN)
	2)Space Complexity: O(N)
	3)Was able to run successfully on leetcode
	4)Having Trouble understanding the Time Complexity of MergeSort 
*/

class MergeSort {
	// Merges two subarrays of arr[].
	// First subarray is arr[l..m]
	// Second subarray is arr[m+1..r]
	void merge(int arr[], int l, int m, int r) {
		// Your code here
		/*
		 * Finding the sizes of subarrays to be merged
		 */
		int n1 = m - l + 1;
		int n2 = r - m;
		/*
		 * Creating temporary sub arrays
		 */
		int L[] = new int[n1];
		int R[] = new int[n2];
		/*
		 * copy the values in the temp arrays
		 */
		for (int i = 0; i < n1; i++) {
			L[i] = arr[l + i];
		}
		for (int j = 0; j < n2; j++) {
			R[j] = arr[m + 1 + j];
		}

		/*
		 * Merging the temp arrays
		 */

		int k = l; // Initializing the initial index of merged array
		int i = 0;
		int j = 0;
		while (i < n1 && j < n2) {
			if (L[i] <= R[j]) {
				arr[k] = L[i];
				i++;
			} else {
				arr[k] = R[j];
				j++;
			}
			k++;
		}
		// Copying remaining items of L
		while (i < n1) {
			arr[k] = L[i];
			i++;
			k++;
		}
		// Copying remaining items of R
		while (j < n2) {
			arr[k] = R[j];
			j++;
			k++;
		}
	}

	// Main function that sorts arr[l..r] using
	// merge()
	void sort(int arr[], int l, int r) {
		// Write your code here
		// Call mergeSort from here

		if (l < r) { // base case or terminating condition
			int middle = l + (r - l) / 2;
			sort(arr, l, middle); // Recursive function called on first half
			sort(arr, middle + 1, r);// Recursive function called on second half
			merge(arr, l, middle, r); // Merge the halves
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