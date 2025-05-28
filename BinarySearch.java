// Time Complexity : O(log n), where n is the number of elements in the array
// Space Complexity : O(1), since we are using constant extra space
// Did this code successfully run on Leetcode : yes
// Any problem you faced while coding this : No

// Your code here along with comments explaining your approach:
// We use the Binary Search algorithm which works only on sorted arrays. 
// The approach repeatedly divides the search interval in half. 
// If the value of the search key is less than the item in the middle of the interval, 
// narrow the interval to the lower half. Otherwise, narrow it to the upper half. 
// Repeated until the value is found or the interval is empty.

class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    {
        //Write your code here
       while(l <= r){
            int mid = (l + r)/2;
            if(x == arr[mid])
            {
                return mid;
            } else if(x < arr[mid]){
                r = mid - 1;
            } else {
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
        int x = 1; 
        int result = ob.binarySearch(arr, 0, n - 1, x); 
        if (result == -1) 
            System.out.println("Element not present"); 
        else
            System.out.println("Element found at index " + result); 
    } 
} 
