// Time Complexity : O(nlogn)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : No

class BinarySearch {
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int A[], int l, int r, int x)
    {
        int mid;
        //Write your code here
        while(l<r){
            mid = l + (r-l)/2;
            if(A[mid] == x)
                return mid;
            else if(A[mid]<x)
                l = mid + 1;
            else
                r = mid - 1;
        }
        if(l == A.length || A[l] !=x)
            return -1;
        return l;
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
