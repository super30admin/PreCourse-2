/*
Author: Akhilesh Borgaonkar
Problem: Implement Binary Search algorithm
Approach: Used iterative approach to perform binary search on input array to find element x.
Time complexity: O(logn) where n is number of elements in array
Space complexity: O(1)
Verified on local machine.
*/

public class Exercise_1 {

    static class BinarySearch {
        // Returns index of x if it is present in arr[l.. r], else return -1
        int binarySearch(int arr[], int l, int r, int x)
        {
            //Write your code here
            while (l<=r) {
                int mid = l + (r - l) / 2;
                if (arr[mid] == x)
                    return mid;
                if (arr[mid] < x)
                    l = mid + 1;
                if (arr[mid] > x)
                    r = mid - 1;
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

}
