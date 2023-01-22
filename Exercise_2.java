// Time Complexity :O(n log n) (average), O(n2) (worst)
// Space Complexity : O(log(n)) 
// Did this code successfully run on Leetcode : yes
// Any problem you faced while coding this : no

/* 
 * Chooses high index value as pivot and swaps all lower values to left 
 * and pivot will be swapped after last swapped value
 * repeat this process for left and right sub array until array gets sorted
 * 
 */
class QuickSort {

	// swaps i and j index values
	void swap(int[] arr, int i, int j) {
		int tempIValue = arr[i];
		arr[i] = arr[j];
		arr[j] = tempIValue;
	}

	// using high value as pivot
	int partition(int[] arr, int low, int high) {
		int pivot = arr[high];
		int i = low;
		for (int j = low; j < high; j++) {
			if (arr[j] <= pivot) {
				swap(arr, i, j);
				i++;
			}
		}
		swap(arr, i, high);
		return i;
	}

	/*
	 * The main function that implements QuickSort() arr[] --> Array to be sorted,
	 * low --> Starting index, high --> Ending index
	 */
	void sort(int[] arr, int low, int high) {
		// Recursively sort elements before
		// partition and after partition
		if (low < high) {
			int partitionIndex = partition(arr, low, high);

			sort(arr, low, partitionIndex - 1);
			sort(arr, partitionIndex + 1, high);
		}
	}

	/* A utility function to print array of size n */
	static void printArray(int[] arr) {
		int n = arr.length;
		for (int i = 0; i < n; ++i)
			System.out.print(arr[i] + " ");
		System.out.println();
	}

	// Driver program
	public static void main(String args[]) {
		int[] arr = { 10, 7, 8, 9, 1, 5 };
		int n = arr.length;

		QuickSort ob = new QuickSort();
		ob.sort(arr, 0, n - 1);

		System.out.println("sorted array");
		printArray(arr);
	}
}
