class MergeSort
{
	// Merges two subarrays of arr[].
	// First subarray is arr[l..m]
	// Second subarray is arr[m+1..r]
	void merge(int arr[], int l, int m, int r)
	{
		int[] tempArray = new int[r - l + 1];
		int i = l, j = m + 1, k = 0;

		while (i <= m && j <= r)
		{
			if (arr[i] <= arr[j])
			{
				tempArray[k] = arr[i];
				k++;
				i++;
			}
			else
			{
				tempArray[k] = arr[j];
				k++;
				j++;
			}

		}

		while (i <= m)
		{
			tempArray[k] = arr[i];
			k++;
			i++;
		}

		while (j <= r)
		{
			tempArray[k] = arr[j];
			k++;
			j++;
		}

		for (i = l; i <= r; i++)
		{
			arr[i] = tempArray[i - l];
		}
	}

	// Main function that sorts arr[l..r] using
	// merge()
	void sort(int arr[], int l, int r)
	{
		if (l < r)
		{
			int mid = (r - l) / 2 + l;
			sort(arr, l, mid);
			sort(arr, mid + 1, r);

			merge(arr, l, mid, r);
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

	// Driver method
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