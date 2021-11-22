
/*
 * * Time Complexity: O(n ^ 2)
 * 
 * Space Complexity: O(n)
 * 
 * This code can run successfully on Leetcode
 * 
 * Any problems you face while coding this - No
 * 
 * Approach: 
 * 1. In this recursive quick sort, we put recursive calls in stack internally which has l and h values
 * 2. In iterative we will define a stack which will have h - l + 1 length
 * 3. We will put l and h values in stack and then we will execute each call till stack is not empty
 * 4. This is same as executing recursive function
 * 5. During execution of each step, we check if there is left subarray and right sub array around pivot whose position
 * 	  we have finalized in partition function. If arrays exist, we put respective low and high bound values in stack
 *
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
		// Compare elements and swap.
		int pivot = arr[h];
		int i = l - 1;

		for (int j = l; j < h; j++) {
			if (arr[j] <= pivot) {
				i++;
				swap(arr, i, j);
			}
		}

		i++;
		swap(arr, i, h);
		return i;
	}

	// Sorts arr[l..h] using iterative QuickSort
	void QuickSort(int arr[], int l, int h) {
		// Try using Stack Data Structure to remove recursion.

		if (l < h) {
			int[] stack = new int[h - l + 1];
			int top = -1;

			top++;
			stack[top] = l;
			top++;
			stack[top] = h;

			while (top != -1) {

				h = stack[top];
				top--;
				l = stack[top];
				top--;

				int pivot = partition(arr, l, h);

				if (pivot - 1 > l) {
					top++;
					stack[top] = l;
					top++;
					stack[top] = pivot - 1;
				}

				if (pivot + 1 < h) {
					top++;
					stack[top] = pivot + 1;
					top++;
					stack[top] = h;
				}
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
