class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
       		if (r >= 1) {
			int mid = l + (r - l) / 2;
			// if the element is present at the middle itself
			if (arr[mid] == x)
				return mid;
			// if the element is smaller than mid, than it can only be present in left sub
			// array
			if (arr[mid] > x)
				return binarySearch(arr, l, mid - 1, x);
			// Else the element can only be present in right sub array
			return binarySearch(arr, mid + 1, r, x);
		}
		// we reach here when element is not present in the array
		return -1;
    } 
  
    // Driver method to test above 
    public static void main(String args[]) 
    { 
        BinarySearch ob = new BinarySearch(); 
        int arr[] = { 2, 3, 4, 10, 40 }; 
        int n = arr.length; 
        int x = 10; 
        int result = ob.binarySearch(arr, 0, n - 1, x); 
        if (result == -1) 
            System.out.println("Element not present"); 
        else
            System.out.println("Element found at index " + result); 
    } 
} 

/*
 * Time Complexity : O(Log n) , T(n) = T(n/2) + c Space Complexity : O(1) in
 * case of iterative implementation and In case of recursive implementation,
 * O(Logn) recursion call stack space.
 */
