class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int mid, int r) 
    {  
       //Your code here  
	   int arr1 = mid - l + 1;
		int arr2 = r - mid;

		int array1[] = new int[arr1];
		int array2[] = new int[arr2];

		for (int i = 0; i < arr1; ++i)
			array1[i] = arr[l + i];
		for (int j = 0; j < arr2; ++j)
			array2[j] = arr[mid + 1 + j];

		int i = 0, j = 0;

		int k = l;
		while (i < arr1 && j < arr2) {
			if (array1[i] <= array2[j]) {
				arr[k] = array1[i];
				i++;
			} else {
				arr[k] = array2[j];
				j++;
			}
			k++;
		}

		while (i < arr1) {
			arr[k] = array1[i];
			i++;
			k++;
		}

		while (j < arr2) {
			arr[k] = array2[j];
			j++;
			k++;
		}
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here 
		if (l < r) {

			int mid = (l + r) / 2;

			sort(arr, l, mid);
			sort(arr, mid + 1, r);

			merge(arr, l, mid, r);
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
        ob.sort(arr, 0, arr.length-1); 
  
        System.out.println("\nSorted array"); 
        printArray(arr); 
    } 
} 