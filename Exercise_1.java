
// Time Complexity : O(logn) everytime we are reducing the search space by 1/2.
// Space Complexity : O(logn) auxiliary stack space for recursion calls, can be eliminated by using while loop.
// Did this code successfully run on Leetcode : n/a
// Any problem you faced while coding this : no


// Your code here along with comments explaining your approach in three sentences only
class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int nums[], int low, int high, int target) 
    { 
        
        //checking when the search is completed and not found the element.
        if(low > high)
            return -1;
        int mid = (low + high)/2;
        //checking if the mid element is the target.
        if(nums[mid] == target)
            return mid;
        /*if not then the element lies either in the left or right part of the array.
        */
        if(nums[mid] > target)
            return binarySearch(nums, low, mid-1, target);
        else
            return binarySearch(nums, mid+1, high,  target);
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
