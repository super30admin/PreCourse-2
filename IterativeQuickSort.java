import java.util.Stack;

class IterativeQuickSort {
	void swap(int arr[], int i, int j) {
		// Try swapping without extra variable

		arr[i] = arr[i] + arr[j];
		arr[j] = arr[i] - arr[j];
		arr[i] = arr[i] - arr[j];
	}

	/*
	 * This function is same in both iterative and recursive
	 */
	int partition(int arr[], int l, int h) {
		// Compare elements and swap.
		// Write code here for Partition and Swap
		int pivot = h;
		int pIndex = l;

		for (int i = l; i < h; i++) {
			if (arr[i] <= arr[pivot]) {
				swap(arr, i, pIndex);
				pIndex++;
			}
		}

		swap(arr, pIndex, pivot);
		return pIndex;
	}

	// Sorts arr[l..h] using iterative QuickSort
	void QuickSort(int arr[], int l, int h) {

		Stack<Integer> stack = new Stack();
		stack.push(l);
		stack.push(h);

		while (!stack.isEmpty()) {
			int high = stack.pop();
			int low = stack.pop();
			if (high - low < 2) {
				if (arr[low] > arr[high]) {
					swap(arr, low, high);
				}
				continue;
			}
			int pivot = partition(arr, low, high);
			stack.push(pivot + 1);
			stack.push(high);

			stack.push(low);
			stack.push(pivot - 1);
		}
	}

	// A utility function to print contents of arr
	void printArr(int arr[], int n) {
		int i;
		for (i = 0; i < n; ++i)
			System.out.print(arr[i] + " ");
	}

	// Driver code to test above
	public static void main(String args[]) {
		IterativeQuickSort ob = new IterativeQuickSort();
		int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 };
		ob.QuickSort(arr, 0, arr.length - 1);
		ob.printArr(arr, arr.length);
	}
}