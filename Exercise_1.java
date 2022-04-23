// Time Complexity : O(logn)
// Space Complexity :O(1)
// Did this code successfully run on Leetcode : No, ran it on the editor.
// Any problem you faced while coding this : No

class BinarySearch {
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
        int mid = 0, index = 0;

        if (l > r) {
            return -1;
        }

        mid = l +(r-l)/2;
        if (arr[mid] == x) {
            return mid;
        } else if (arr[mid] > x) {
            r = mid - 1;
        } else {
            l = mid + 1;
        }

        index = binarySearch(arr, l, r, x);

        return index;
    } 
  
    // Driver method to test above 
    public static void main(String args[]) 
    { 
        BinarySearch ob = new BinarySearch(); 
        int arr[] = { 2, 3, 4, 10, 40 }; 
        int n = arr.length; 
        int x = 4;
        int result = ob.binarySearch(arr, 0, n - 1, x); 
        if (result == -1) 
            System.out.println("Element not present"); 
        else
            System.out.println("Element found at index " + result); 
    } 
} 
