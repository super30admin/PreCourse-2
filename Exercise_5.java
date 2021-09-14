class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
	{ 
		//Try swapping without extra variable 
		System.out.println(arr[i] + " and " + arr[j]);
		arr[i] = arr[i] ^ arr[j];
		arr[j] = arr[i] ^ arr[j]; 
		arr[i] = arr[i] ^ arr[j]; 
 
        System.out.println(arr[i] + " and " + arr[j]);
		
	} 

	/* This function is same in both iterative and 
       recursive*/
	int partition(int arr[], int l, int h) 
	{ 
		//Compare elements and swap.
		int top = arr[h];
		int indx = (l - 1);
		for (int i = l; i <= h - 1; i++) {
			if (arr[i] <= top) {
				indx++;
				int tmp = arr[indx];
				arr[indx] = arr[i];
				arr[i] = tmp;
			}
		}

		int tmp = arr[indx + 1];
		arr[indx + 1] = arr[h];
		arr[h] = tmp;

		return indx + 1;
	} 

	// Sorts arr[l..h] using iterative QuickSort 
	void QuickSort(int arr[], int l, int h) 
	{ 
		//Try using Stack Data Structure to remove recursion.
		if (l < h) {
			int mid = partition(arr, l, h);

			QuickSort(arr, l, mid - 1);
			QuickSort(arr, mid + 1, h);
		}
	} 
  
    // A utility function to print contents of arr 
    void printArr(int arr[], int n) 
    { 
        int i; 
        for (i = 0; i < n; ++i) 
            System.out.print(arr[i] + " "); 
    } 
  
    // Driver code to test above 
    public static void main(String args[]) 
    { 
        IterativeQuickSort ob = new IterativeQuickSort(); 
        int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 }; 
        ob.QuickSort(arr, 0, arr.length - 1); 
        ob.printArr(arr, arr.length); 
    } 
} 