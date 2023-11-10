class MergeSort {
	// Merges two subarrays of arr[].
	// First subarray is arr[l..m]
	// Second subarray is arr[m+1..r]
	void merge(int arr[], int l, int m, int r) {

		// Find size of the two sorted arrays 
		int leftSize = m - l + 1;
		int rightSize = r - m;

		// make temp arrays 
	
		int[] leftArr = new int[leftSize];
		int[] rightArr = new int[rightSize];

		// fill temp arrays
		for (int i = 0; i < leftSize; ++i) {
			leftArr[i] = arr[l + i];
		}
		for (int j = 0; j < rightSize; ++j) {
			rightArr[j] = arr[m +1 + j];
		}

		int i = 0, j = 0;

		int k = l;
		// nor merge these temp sorted arrays 
		while (i < leftSize && j<rightSize) {

			if (leftArr[i] <= rightArr[j]) {
				arr[k] = leftArr[i];
				i++;
			}else {
				arr[k] = rightArr[j];
				j++;
			}
				
			k++;
		}

		while(i<leftSize) {
			arr[k]= leftArr[i];
			k++;
			i++;
		}
		while(j<rightSize) {
			arr[k]= rightArr[j];
			k++;
			j++;
		}
		
	}

	// Main function that sorts arr[l..r] using
	// merge()
	void sort(int arr[], int l, int r) {
		// Write your code here	
		if (l < r) {
			int mid = l + (r - l) / 2;
			sort(arr, l, mid);
			sort(arr, mid + 1, r);
			merge(arr, l, mid, r);
		} 
		

	}

	/* A utility function to print array of size n */
	static void printArray(int arr[]) {
		int n = arr.length;
		for (int i = 0; i < n; ++i)
			System.out.print(arr[i] + " ");
		System.out.println();
	}

	// Driver method
	public static void main(String args[]) {
		int arr[] = { 12, 11, 13, 5, 6, 7 };

		System.out.println("Given Array");
		printArray(arr);

		MergeSort ob = new MergeSort();
		ob.sort(arr, 0, arr.length - 1);

		System.out.println("\nSorted array");
		printArray(arr);
	}
}