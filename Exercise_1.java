// Time Complexity : O(N)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this :
// The conditions change when you change the value of the right position.
// It can be either r=nums.length or r=nums.length-1. The other if conditions 
// in binary search have to be modified based on this initial condition.


// Your code here along with comments explaining your approach




class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        int mid;
        while(l<=r){
            mid=l+(r-l)/2;
            if(x==arr[mid]) return mid;
            if(x<arr[mid])  r=mid-1;
            else l=mid+1;
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
