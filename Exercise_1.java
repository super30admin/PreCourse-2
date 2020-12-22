/*
Binary Search in Sorted Array:
Time complexity: O(log n), as we are dividing the array into 2 halves and performing search based on mid point
 // Time Complexity : O(log n)
// Space Complexity : O(1), as we not using any extra space to store elements. But
// Did this code successfully run on Leetcode :
// Any problem you faced while coding this : No
 */
class BinarySearch {
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
        while (l <= r){
            //find mid point of array
            int mid = (l + r) /2;
            //if the element present at mid index is key, then return mid index
            if (arr[mid] == x){
                return mid;
            }
            // if mid element is less than key, then search on right
            else if (arr[mid] < x){
                l = mid+1;
            }else{ //else search on left
                r = mid-1;
            }
        }
        return -1;
    } 
  
    // Driver method to test above 
    public static void main(String args[]) 
    { 
        BinarySearch ob = new BinarySearch(); 
        //int arr[] = { 2, 3, 4, 10, 40 };
        int arr[] = {40};
        int n = arr.length; 
        int x = 40;
        int result = ob.binarySearch(arr, 0, n - 1, x); 
        if (result == -1) 
            System.out.println("Element not present"); 
        else
            System.out.println("Element found at index " + result); 
    } 
} 
