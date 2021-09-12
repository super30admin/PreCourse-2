class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
	{
		if (arr.length == 0) {
			return -1;
		}

		int mid = l + (r - l) / 2;

		if (arr[mid] == x) {
			return mid;
		} else if (x < arr[mid]) {
			return binarySearch(arr, l, mid, x);
		} else if (x > arr[mid]) {
			return binarySearch(arr, mid + 1, r, x);
		} else {
			return -1;
		}

	}
  
    // Driver method to test above 
    public static void main(String args[]) 
    { 
        BinarySearch ob = new BinarySearch(); 
        int arr[] = { 2, 3, 4, 5, 7, 9, 10, 12, 17, 25, 30, 39, 40 , 55}; 
        int n = arr.length; 
        int x = 40; 
        int result = ob.binarySearch(arr, 0, n - 1, x); 
        if (result == -1) 
            System.out.println("Element not present"); 
        else
            System.out.println("Element found at index " + result); 
    } 
} 
