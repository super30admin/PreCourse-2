class MergeSort 
{ 
	private static void mergeSort(int[] arr) {
		if (arr.length == 1)
			return;
		int middle = arr.length / 2;

		// create two sub arrays
		int[] left = new int[middle];
		for (int i = 0; i < middle; i++) {
			left[i] = arr[i];
		}

		int[] right = new int[arr.length - middle];
		for (int i = middle; i < arr.length; i++) {
			right[i - middle] = arr[i];
		}

		mergeSort(left);
		mergeSort(right);

		merge(left, right, arr);
	}

	private static void merge(int[] left, int[] right, int[] result) {
		int i = 0, j = 0, k = 0;
		while (i < left.length && j < right.length) {
			if (left[i] <= right[j])
				result[k++] = left[i++];
			else
				result[k++] = right[j++];
		}

		while (i < left.length) {
			result[k++] = left[i++];
		}
		while (j < right.length) {
			result[k++] = right[j++];
		}

	}
  
    /* A utility function to print array of size n */
    static void printArray(int arr[]) 
    { 
        int n = arr.length; 
        for (int i=0; i<n; ++i) 
            System.out.print(arr[i] + " "); 
        System.out.println(); 
    } 
  
    // Driver method 
    public static void main(String args[]) 
    { 
        int arr[] = {12, 11, 13, 5, 6, 7}; 
  
        System.out.println("Given Array"); 
        printArray(arr); 
  
        MergeSort ob = new MergeSort(); 
        ob.mergeSort(arr); 
  
        System.out.println("\nSorted array"); 
        printArray(arr); 
    } 
} 