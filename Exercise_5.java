/**
 *	Time Complexity : O(nlogn)
 *	worst case : O(n2)
 *
 * 1. Take last element in array as reference
 * 2. loop through from start element to last element if element is less than last swap it
 * 3. place the last element in the right place
 * 4. sort left and right sub arrays from partition index
 */

class IterativeQuickSort {
	void swap(int arr[], int i, int j) {
		// Try swapping without extra variable
		if (i != j) {
			arr[i] = arr[i] + arr[j];
			arr[j] = arr[i] - arr[j];
			arr[i] = arr[i] - arr[j];
		}
	}

	/*
	 * This function is same in both iterative and recursive
	 */
	int partition(int arr[], int l, int h) {
		// take last element
		int last = arr[h];
		int index = (l - 1);
		for (int j = l; j <= h - 1; j++) {
			if (arr[j] < last) {
				index++;
				swap(arr, index, j);
			}
		}
		swap(arr, index + 1, h);
		return (index + 1);
	}

	// Sorts arr[l..h] using iterative QuickSort
	void QuickSort(int arr[], int l, int h) {
		if (l < h) {
			int parIndex = partition(arr, l, h);

			QuickSort(arr, l, parIndex - 1);
			QuickSort(arr, parIndex + 1, h);
		}
	}

	// A utility function to print contents of arr
	void printArr(int arr[], int n) {
		int i;
		for (i = 0; i < n; ++i)
			System.out.print(arr[i] + " ");
	}
}

public class Exercise_5 {
	// Driver code to test above
	public static void main(String args[]) {
		IterativeQuickSort ob = new IterativeQuickSort();
		int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 };
		ob.QuickSort(arr, 0, arr.length - 1);
		ob.printArr(arr, arr.length);
	}

}