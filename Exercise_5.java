/*
   QuickSort(Iterative)
	1)Time Complexity: Worst-case : O(N^2)
	2)Space Complexity: Worst-case: O(N)
	3)Was able to run successfully on leetcode
	4)Having trouble understanding best case and average case time complexity and space complexity
*/
class IterativeQuickSort {

	/*
	 * This function is same in both iterative and recursive
	 */
	int partition(int arr[], int l, int h) {
		// Compare elements and swap.
		int pivot = arr[h];// Setting the last element as Pivot
		int i = l - 1;// index of smaller element
		for (int j = l; j < h; j++) {
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
		arr[i + 1] = arr[h];
		arr[h] = temp;
		return i + 1;
	}

	// Sorts arr[l..h] using iterative QuickSort
	void QuickSort(int arr[], int l, int h) {
		int Stack[] = new int[h - l + 1]; // creating auxillary stack
		int top = -1; // Initializing top of the stack as -1
		// Push Initial Values of l and h onto the stack
		Stack[++top] = l;
		Stack[++top] = h;
		// Keep popping till stack is not empty
		while (top >= 0) {
			// pop h and l
			h = Stack[top--];
			l = Stack[top--];
			// Set Pivot at it's correct position in sorted array
			int pivot = partition(arr, l, h);
			// If there are elements on left side, push left side onto stack
			if (pivot - 1 > l) {
				Stack[++top] = l;
				Stack[++top] = pivot - 1;
			}
			// If there are elements on right side, push right side onto stack
			if (pivot + 1 < h) {
				Stack[++top] = pivot + 1;
				Stack[++top] = h;
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
		IterativeQuickSort ob = new IterativeQuickSort();
		int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 };
		ob.QuickSort(arr, 0, arr.length - 1);
		ob.printArr(arr, arr.length);
	}
}