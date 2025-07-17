// Time Complexity : O(logn)
// Space Complexity : O(logn) since its recursive
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : no
// Your code here along with comments explaining your approach
class BinarySearch {
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
        // if the start and end indices cross over, we assume the element is not found during the search and return -1
        if(l>r) {
            return -1;
        }

        // calculate the mid point of the indices
        int mid = l+(r-l)/2;

        // check if the value is found and return the index
        if(arr[mid]==x) {
            return mid;
        // check if the value is greater, then decrease the right pointer
        } else if (arr[mid]>x) {
            r = mid-1;
        // check if the value is lesser, then increase the left pointer
        } else {
            l = mid+1;
        }
        // recursively call the same method with new search space
        return binarySearch(arr, l, r, x);
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
