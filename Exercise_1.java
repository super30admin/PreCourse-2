// Time Complexity : O(logn)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : yes
// Any problem you faced while coding this : 
// l<r or l<=r
// l = mid+1; or l = mid;


// Your code here along with comments explaining your approach
// if mid is target then return mid, if mid element is leass than target then target will be on right else
// target will be on left. if l>r then target is not there in array

class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        while(l<=r){
            int mid = l + (r-l)/2;
            if(arr[mid] == x) return mid;
            if(arr[mid]<x) l = mid+1;
            else r = mid-1;
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
