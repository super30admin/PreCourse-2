// Time Complexity : O(NlogN) N is the number of elements in the array.
// Space Complexity : O(logN) for recursion
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : None


// Your code here along with comments explaining your approach


/**
 * @author akhilreddy619
 * In quick sort, we have to partition the array into two parts every time by finding
 * pivot index which separates smaller elements on one side and bigger elements (than pivot)
 * on the other side. To find pivot index, we consider last element as pivot element. And we
 * maintain a variable to track the index of the smaller elements that are less than pivot element with i.
 * Then iterate over from low to high - 1 elements to check if any element is <= pivot.
 * If found, we swap the current index with ith index. After all iterations we swap i+1th 
 * index with pivot such that pivot separates smaller elements and bigger elements than the pivot.
 * Repeat the process for the elements ranging from (low, pivot index - 1) and (pivot index + 1, high).
 */
class QuickSort {
	/*
	 * This function takes last element as pivot, places the pivot element at its
	 * correct position in sorted array, and places all smaller (smaller than pivot)
	 * to left of pivot and all greater elements to right of pivot
	 */
	void swap(int arr[], int i, int j) {
		// Your code here
		int temp = arr[i];
		arr[i] = arr[j];
		arr[j] = temp;
	}

	int partition(int arr[], int low, int high) {
		// Write code here for Partition and Swap
		int pivot = arr[high];
		int i = low - 1;
		for (int j = low; j <= high - 1; j++) {
			if (arr[j] <= pivot) {
				i++;
				swap(arr, i, j);
			}
		}
		swap(arr, i + 1, high);
		return (i+1);
	}

	/*
	 * The main function that implements QuickSort() arr[] --> Array to be sorted,
	 * low --> Starting index, high --> Ending index
	 */
	void sort(int arr[], int low, int high) {
		// Recursively sort elements before
		// partition and after partition
		if (low >= high)
			return;
		int pivot = partition(arr, low, high);
		sort(arr, low, pivot - 1);
		sort(arr, pivot + 1, high);
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
		int arr[] = { 2, 10, 7, 8, 9, 1, 5 };
		int n = arr.length;

		QuickSort ob = new QuickSort();
		ob.sort(arr, 0, n - 1);

		System.out.println("sorted array");
		printArray(arr);
	}
}
