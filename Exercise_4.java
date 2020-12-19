/* Java program for Merge Sort */
class MergeSort 
{
	
	void merge(int arr[], int l, int m, int r)
	{
	
		int sizeleftarray = m - l + 1;
		int sizerightarray = r - m;

	
		int left[] = new int[sizeleftarray];
		int right[] = new int[sizerightarray];

			for (int i = 0; i < sizeleftarray; ++i)
				left[i] = arr[l + i];
		for (int j = 0; j < sizerightarray; ++j)
			right[j] = arr[m + 1 + j];

	
		int i = 0, j = 0;

	
		int k = l;
		while (i < sizeleftarray && j < sizerightarray) {
			if (left[i] <= right[j]) {
				arr[k] = left[i];
				i++;
			}
			else {
				arr[k] = right[j];
				j++;
			}
			k++;
		}

		while (i < sizeleftarray) {
			arr[k] = left[i];
			i++;
			k++;
		}

	
		while (j < sizerightarray) {
			arr[k] = right[j];
			j++;
			k++;
		}
	}

	
	void sort(int arr[], int l, int r)
	{
		if (l < r) {
			// Find the middle point
			int m = (l + r) / 2;
			System.out.println("l="+l+"r="+r+"m="+m);
			// Sort first and second halves
			sort(arr, l, m);
			System.out.println("l="+l+"r="+r+"m="+m);
			sort(arr, m + 1, r);

			// Merge the sorted halves
			merge(arr, l, m, r);
		}
	}

	/* A utility function to print array of size n */
	static void printArray(int arr[])
	{
		int n = arr.length;
		for (int i = 0; i < n; ++i)
			System.out.print(arr[i] + " ");
		System.out.println();
	}

	// Driver code
	public static void main(String args[])
	{
		int arr[] = { 12, 11, 13, 5, 6, 7 };

		System.out.println("Given Array");
		printArray(arr);

		MergeSort ob = new MergeSort();
		ob.sort(arr, 0, arr.length - 1);

		System.out.println("\nSorted array");
		printArray(arr);
	}
}
/* This code is contributed by Rajat Mishra */
