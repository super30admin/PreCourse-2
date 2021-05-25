/**
 *	Time Complexity : O(nlogn)
 *	worst case : O(n2)
 *
 * 1. Take last element in array as reference
 * 2. loop through from start element to last element if element is less than last swap it
 * 3. place the last element in the right place
 * 4. sort left and right sub arrays from partition index
 */

class QuickSort {
	/*
	 * This function takes last element as pivot, places the pivot element at its
	 * correct position in sorted array, and places all smaller (smaller than pivot)
	 * to left of pivot and all greater elements to right of pivot
	 */
	void swap(int arr[], int i, int j) {
		int temp = arr[i];
		arr[i] = arr[j];
		arr[j] = temp;
	}

	int partition(int arr[], int low, int high) {
		
		//take last element
		int last = arr[high];
		int index = (low - 1);
		for (int j = low; j <= high - 1; j++) {
			if (arr[j] < last) {
				index++;
				swap(arr, index, j);
			}
		}
		swap(arr, index + 1, high);
		return (index + 1);
	}

	/*
	 * The main function that implements QuickSort() arr[] --> Array to be sorted,
	 * low --> Starting index, high --> Ending index
	 */
	void sort(int arr[], int low, int high) {
		if (low < high) {
			int parIndex = partition(arr, low, high);

			sort(arr, low, parIndex - 1);
			sort(arr, parIndex + 1, high);
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

public class Exercise_2 {
	// Driver program
	public static void main(String args[]) {
		int arr[] = { 10, 7, 8, 9, 1, 5 };
		int n = arr.length;

		QuickSort ob = new QuickSort();
		ob.sort(arr, 0, n - 1);

		System.out.println("sorted array");
		QuickSort.printArray(arr);
	}

}
