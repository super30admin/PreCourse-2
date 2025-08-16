// Time Complexity : O(log n)
// Space Complexity : O(1) since we are not using extra space for storing the elements
// Did this code successfully run on Leetcode : yes
// Any problem you faced while coding this : no


// Your code here along with comments explaining your approach
// Using the indexes in sorted array to not look at half of elements in each iteration
// Doing "l + (r-l)/2" instead of "l + r/2" to avoid number out of range exception
class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
        while (l <=r) {
            int mid = l  + (r -l) /2;
            if (arr[mid] == x)
                return mid;
            
            if (arr[mid] < x)
                l = mid + 1;
            else
                r = mid -1;
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
