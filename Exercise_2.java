public class QuickSortAlgo {

	int partition(int arr[], int low, int high) {
		int pivot = arr[high];
		int i = (low - 1);
		for (int j = low; j < high; j++) {
			if (arr[j] < pivot) {
				i++;
				int temp = arr[j];
				arr[j] = arr[i];
				arr[i] = temp;
			}
		}
		int temp1 = arr[i + 1];
		arr[i + 1] = arr[high];
		arr[high] = temp1;
		return i + 1; 
	}

	void sort(int arr[], int low, int high) {
		if(low<high) {
		int pivotindex = partition(arr, low, high);
		sort(arr, low, pivotindex-1);
		sort(arr, pivotindex + 1, high);
	}
	}


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

		QuickSortAlgo ob = new QuickSortAlgo();
		ob.sort(arr, 0, n - 1);

		System.out.println("sorted array");
		printArray(arr);
	}

}
