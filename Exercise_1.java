/*Time complexity
Binary Search - O(logn) as we are halving the search space at every recursive call
*/

/*Space complexity
O(1) as we do not use any additional data structure
*/

// Did this code successfully run on Leetcode : Yes.

// Any problem you faced while coding this : None
class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
        int mid = (l + r) / 2;

        if (l > r)
            return -1;
        if (arr[mid] == x) {
            return mid;
        } else if (arr[mid] < x) {
            return binarySearch(arr, mid + 1, r, x);

        } else if (arr[mid] > x) {
            return binarySearch(arr, l, mid - 1, x);
        } else
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
