// Time Complexity : o(log n)
// Space Complexity :o(1)
// Did this code successfully run on Leetcode : N/A it is not a leetcode problem
// Any problem you faced while coding this :no


// Your code here along with comments explaining your approach
//1. consider left pointer at 0th index and right pointer at last index and middle of both.
//2.  iterate until left and right not crossing 
//3. check if target is matching with mid element, if yes return mid index.
//4. Else if target is greater than mid element then check the target on right side of of mid, else go towards left side.

class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        while(l<=r){
            int mid = l+(r-l)/2;
            if(arr[mid]== x){
                return mid;
            }else if(arr[mid]<x){
                l = mid+1;
            }else{
                r = mid-1;
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
