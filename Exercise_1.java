// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : No
class BinarySearch {
    // Returns index of x if it is present in arr[l.. r], else return -1
    // Recursive approach
    // Time Complexity - O(log N) N is the size of the array
    // Space Complexity - O(1)
   /* int binarySearch(int arr[], int l, int r, int x)
    { 
        //Write your code here
        if( r >= l) {
            int mid = l + (r-l) / 2;
            if (arr[mid] == x) {
                return mid;
                return mid;
            }
            if (x > arr[mid]) {
                return binarySearch(arr,mid+1,r,x);
            }
            return binarySearch(arr,l,mid-1,x);
        }
        return -1;
    }*/

    // Iterative approach
    // Time Complexity - O(log N)
    // Space complexity - O(1)
    int binarySearch(int arr[], int l, int r, int x)
    {
        //Write your code here
        while( l <= r) {
            int mid = l + (r-l) / 2;
            if (arr[mid] == x) {
                return mid;
            }else if( arr[mid] > x) {
                r = mid-1;
            }else{
                l = mid + 1;
            }

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
