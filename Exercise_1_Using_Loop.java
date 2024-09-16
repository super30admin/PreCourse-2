package com.precourse2;

public class BinarySearchAlgoUsingLoop {

	// Returns index of x if it is present in arr[l.. r], else return -1
	int binarySearch(int arr[], int l, int r, int x) {
		// Write your code here
		if (arr[r / 2] == x) {
			return arr[r / 2];
		} else if (arr[r / 2] > x) {
			for (int i = 0; i < r / 2; i++) {
				if (arr[i] == x) {
					return i;
				}
			}
		} else {
			for (int j = r / 2; j <= r; j++) {
				if (arr[j] == x) {
					return j;
				}
			}
		}
		return -1;
	}

	// Driver method to test above
	public static void main(String args[]) {
		BinarySearchAlgoUsingLoop ob = new BinarySearchAlgoUsingLoop();
		int arr[] = { 2, 3, 4, 10, 40 };
		int n = arr.length;
		int x =2 ;
		int result = ob.binarySearch(arr, 0, n - 1, x);
		if (result == -1)
			System.out.println("Element not present");
		else
			System.out.println("Element found at index " + result);
	}
}
