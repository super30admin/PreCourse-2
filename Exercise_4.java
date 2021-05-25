/**
 * Time Complexity : O(nLogn)
 *
 * 1. find middle index and divide array to two halfs from middle index 
 * 2. recursively sort sub array and merge
 * 3. print the sorted array at the end
 */

class MergeSort {
	// Merges two subarrays of arr[].
	// First subarray is arr[l..m]
	// Second subarray is arr[m+1..r]
	void merge(int arr[], int l, int m, int r) {
		int leftLen = m - l + 1;
		int rightLen = r - m;

		int leftArr[] = new int[leftLen];
		int rightArr[] = new int[rightLen];

		System.arraycopy(arr, l, leftArr, 0, leftLen);
		System.arraycopy(arr, m + 1, rightArr, 0, rightLen);

		int i = 0, j = 0;
		int index = l;
		while (i < leftLen && j < rightLen) {
			if (leftArr[i] <= rightArr[j]) {
				arr[index++] = leftArr[i++];
			} else {
				arr[index++] = rightArr[j++];
			}
		}

		//copy remaining arrays first left than right
		while (i < leftLen) {
			arr[index++] = leftArr[i++];
		}
		while (j < rightLen) {
			arr[index++] = rightArr[j++];
		}
	}

	// Main function that sorts arr[l..r] using
	// merge()
	void sort(int arr[], int l, int r) {
		if (l < r) {
			// Find the middle point
			int m = l + (r - l) / 2;

			// Sort first and second halves
			sort(arr, l, m);
			sort(arr, m + 1, r);

			// Merge the sorted halves
			merge(arr, l, m, r);
		}
	}

	/* A utility function to print array of size n */
	static void printArray(int arr[]) {
		int n = arr.length;
		for (int i = 0; i < n; ++i)
			System.out.print(arr[i] + " ");
		System.out.println();
	}
}

public class Exercise_4 {
	// Driver method
	public static void main(String args[]) {
		int arr[] = { 12, 11, 13, 5, 6, 7 };

		System.out.println("Given Array");
		MergeSort.printArray(arr);

		MergeSort ob = new MergeSort();
		ob.sort(arr, 0, arr.length - 1);

		System.out.println("\nSorted array");
		MergeSort.printArray(arr);
	}

}