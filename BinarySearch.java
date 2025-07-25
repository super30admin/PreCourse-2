/**
 * space complexity: O(log n)
 * time complexity: O(log n)
 * did this code successfully run on Leetcode: This is not a Leetcode problem
 * any problem you faced while coding this: No
 *
 * This is a Java program that implements binary search on a sorted array.
 * It includes a method to perform the search and a main method to test it.
 */


class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
          if (r >= l) 
          { 
          /** Find the mid index
           * The mid index is calculated to avoid overflow
           */
          int mid = l + (r - l) / 2; 
          

        /** If the element is present at the middle itself 
         *  Return the middle index if the element is found
         */
            if (arr[mid] == x) 
                return mid; 
        
        /** If the element is smaller than mid, then it can only be present in left subarray 
         * Call the binary search recursively on the left subarray 
         */
            if (arr[mid] > x) 
                return binarySearch(arr, l, mid - 1, x); 

        /** Else the element can only be present in right subarray
         * Call the binary search recursively on the right subarray
         * (With each call reduce the search space by half until the middle element of the array is the target element)*/
            return binarySearch(arr, mid + 1, r, x); 
        } 
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
