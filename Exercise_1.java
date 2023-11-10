// Time Complexity :O(nlogn) if sort the input array first otherwise if it is already sorted then O(logn)
// Space Complexity :O(n)
// Did this code successfully run on Leetcode : N/A
// Any problem you faced while coding this : No

import java.util.Arrays;
import java.util.Collections;

class BinarySearch {
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) {
        //Write your code here
        Arrays.sort(arr); // sorting array in ascending order
        int mid = (l + r) / 2; // calculating mid element
        if (x > arr[mid]) { // if x > mid, then search in right half
            mid++;
            return binarySearch(arr,mid, r, x);
        } else if (x < arr[mid]) { // if x < mid search in left half
            mid--;
            return binarySearch(arr,l, mid, x);
        } else if (x == arr[mid]) // if mid == x, then return result
            return mid;

        return 0; // if not found return 0
    }
  
    // Driver method to test above 
//    public static void main(String args[])
//    {
//        BinarySearch ob = new BinarySearch();
//        int arr[] = { 2, 3, 4, 10, 40 };
//        int n = arr.length;
//        int x = 10;
//        int result = ob.binarySearch(arr, 0, n - 1, x);
//        if (result == -1)
//            System.out.println("Element not present");
//        else
//            System.out.println("Element found at index " + result);
//    }
} 
