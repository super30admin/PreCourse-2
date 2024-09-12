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
           
            while (l<=r) { 			//not letting left and right pointers cross
                int mid = l + (r - l) / 2;	//finding mid element to reduce number of iterations
                if (arr[mid] == x)		//if element found at mid
                    return mid;
                if (arr[mid] < x)		//if element is greater than mid then we know that we need to search in right half of mid
                    l = mid + 1;		//so we assign our left ptr to mid+1
                if (arr[mid] > x)		//if element is less than mid element then we need to search for element in left half of mid
                    r = mid - 1;		//so we assign right ptr to mid-1
            }
            return -1;				//if element not found then return -1
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
