// Time Complexity : O(log n)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : None

class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 

        while (l <= r) {
            //find middle of the array
            int m = (l + r) / 2;
            
            //if the elment is at the middle of the array
            if (arr[m] == x) {
                return m;

           //if element is less than the middle element, it lies in the left subarray
            } else if (arr[m] > x) {
                r = m - 1;
            
            } else {
              //if element is greater than the middle element, it lies in the right subarray

              l = m + 1;
            }  
        }

        // Element not Found
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
