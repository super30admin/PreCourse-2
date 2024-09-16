/*
   QuickSort(Recursive)
	1)Time Complexity: Worst-case: O(N^2)
	2)Space Complexity: Worst-case: 
	3)Was able to run successfully on leetcode
	4)Having trouble understanding best case and average case time        	complexity and space complexity
*/

class QuickSort {
	/*
	 * This function takes last element as pivot, places the pivot element at its
	 * correct position in sorted array, and places all smaller (smaller than pivot)
	 * to left of pivot and all greater elements to right of pivot
	 */

	int partition(int arr[], int low, int high) {
		// Write code here for Partition and Swap
		int pivot = arr[high]; // Setting the last element as Pivot
		int i = low - 1; // index of smaller element
		for (int j = low; j < high; j++) {
			// checking if current element is smaller than pivot
			if (arr[j] < pivot) {
				i++;
				// swapping
				int temp = arr[i];
				arr[i] = arr[j];
				arr[j] = temp;
			}
		}
		// swapping arr[i+1] and pivot
		int temp = arr[i + 1];
		arr[i + 1] = arr[high];
		arr[high] = temp;
		return i + 1;
	}

	/*
	 * The main function that implements QuickSort() arr[] --> Array to be sorted,
	 * low --> Starting index, high --> Ending index
	 */
	void sort(int arr[], int low, int high) {
		// Recursively sort elements before
		// partition and after partition
		if (low < high) { // base case for the recursive function
			int pivot = partition(arr, low, high); // getting the pivot
			sort(arr, low, pivot - 1); // before partition
			sort(arr, pivot + 1, high); // After Partition
		}
	}

	/* A utility function to print array of size n */
	static void printArray(int arr[]) {
		int n = arr.length;
		for (int i = 0; i < n; ++i)
			System.out.print(arr[i] + " ");
		System.out.println();
	}

	// Driver program
	public static void main(String args[]) {
		int arr[] = { 10, 7, 8, 9, 1, 5 };
		int n = arr.length;

		QuickSort ob = new QuickSort();
		ob.sort(arr, 0, n - 1);

		System.out.println("sorted array");
		printArray(arr);
	}
}
