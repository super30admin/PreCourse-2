// Time Complexity : O(logn) (where n is the number of elements in the array)
// Space Complexity : O(n) (array size)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : No


class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
        // Continue, if left is less than right 
        while (l < r) {
            int mid = l + (r-l)/2; // find mid and check if mid value is equal to x, if equal return
            if (arr[mid] == x) {
            return mid;        
            }
            else if (arr[mid] < x) { // else, check if mid value is greater than x, if yes, search for x after mid (right of mid)
                l = mid+1; // update l value = mid + 1
            }
            else { // else search for x before mid (left of mid)
                r = mid-1; // update r value to mid - 1 
            }
        } return -1; 

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
