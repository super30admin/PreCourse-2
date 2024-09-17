// Time Complexity : O(nlogn) for all operations
// Space Complexity : O(n) -> n is the maximum stack size
// Did this code successfully run on Leetcode : 
// Any problem you faced while coding this : No

public class Exercise_5 {
	void swap(int arr[], int i, int j) {
		if (i != j) {
			arr[i] = arr[i] + arr[j];
			arr[j] = arr[i] - arr[j];
			arr[i] = arr[i] - arr[j];
		}
	}

	/*
	 * Given a pivot x, put all elements less than x on one side of array and all
	 * elements greater than x on the other side.
	 */
	int partition(int arr[], int l, int h) {
		int pivot = arr[h];
		int i = (l - 1); // index of smaller element
		for (int j = l; j < h; j++) {
			if (arr[j] <= pivot) {
				i++;
				swap(arr, i, j);
			}
		}
		swap(arr, i + 1, h);
		return i + 1;
	}

	// Sorts arr[l..h] using iterative QuickSort
	void QuickSort(int arr[], int low, int high) {
		// Similar to recursion. Use a stack to simulate recursive quicksort
		int[] stack = new int[high - low + 1];
		int top = -1;
		stack[++top] = low;
		stack[++top] = high;

		while (top >= 0) {
			// Get high and low from stack top for each iteration
			high = stack[top--];
			low = stack[top--];

			// Partition the array.
			int pivot = partition(arr, low, high);
			// Push elements less than pivot to stack
			if (pivot - 1 > low) {
				stack[++top] = low;
				stack[++top] = pivot - 1;
			}

			// Push elements greater than pivot to stack
			if (pivot + 1 < high) {
				stack[++top] = pivot + 1;
				stack[++top] = high;
			}
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
		Exercise_5 ob = new Exercise_5();
		int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 };
		ob.QuickSort(arr, 0, arr.length - 1);
		ob.printArr(arr, arr.length);
	}
}