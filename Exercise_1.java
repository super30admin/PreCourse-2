// Time Complexity : In either of recursive or iterative solution we are taking only one half of the array causing a /2 at each step (i.e) O(log n)
// Space Complexity : Only an additional mid constant is required, so space complexity: O(1)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : Received Time limit exceeded on Leetcode as I was trying to search on left half ending with mid rather than mid-1
// Could not identify when to use (l+r)/2 and when l+ (r-l)/2

// Your code here along with comments explaining your approach
class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here

        // Recursive solution where we assign mid to be left index+right index divided by 2 and compare the search value if it is same as mid / lesser or greater.
        // Write your code here
        // if(arr == null) return -1;
        
        // if(l > r) return -1;
        // int mid = l+(r-l)/2;
        // if(x==arr[mid]) {
        //      return mid;
        // }
        // else if(x<arr[mid]) {
        //      return binarySearch(arr, l, mid-1, x);
        //  }
        // else if(x>arr[mid]) {
        //      return binarySearch(arr, mid+1, r, x);
        // }
        // return -1;

        // Iterative solution keeps running until ending index is greater than or equal to start index
        while(l<=r) {
            // getting mid value as (left index + right index) /2
            int mid = l+(r-l)/2;
            // if search value equals mid element return mid index.
            if(x==arr[mid]) {
                return mid;
            }
            // else update right index to be mid and run iteration.
            if(x<arr[mid]) {
                r = mid-1;
            }
            // else update left index to be mid+1 and run iteration.
            else {
                l = mid+1;
            }
        }
        // if right index becomes lesser than left index, return -1
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
