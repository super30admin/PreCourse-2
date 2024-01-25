// Time Complexity : O(logn) and for Arrays.sort() O(nlogn)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : Yes without doing sorting
// Any problem you faced while coding this : No


// Your code here along with comments explaining your approach
/*
 * Its not mentioned that array is sorted
 * Henced I used Arrays.sort()
 * 
 * I've dividing the array in 2 parts and checking if the mid-point is target value
 * If not
 * If target is greater the array[mid-point] then I discard the left array and shift my left pointer by mid-point + 1
 * If target is lesset the array[mid-point] then I discard the right array and reduce my right pointer by mid-point - 1
 * 
 * and continue this process till my left pointer <= right pointer
 * If still not found then I return "-1"
*/

import java.util.Arrays;

class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        Arrays.sort(arr);
        
        while(l <= r) {
            int mid = l + (r - l) / 2;
            
            if (arr[mid] == x) {
                return mid;
            } 

            if (arr[mid] < x) {
                l = mid + 1;
            } else {
                r = mid -1;
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
