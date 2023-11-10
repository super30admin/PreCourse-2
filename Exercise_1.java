// Time Complexity : O(logn)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : Not applicable
// Any problem you faced while coding this : no

// Approach : find the middle element if the target matches the middle elemet return it
// if the middle element is greater than the target then perform binarySearch on 0 and m-1 as left and right
// if the middle element is less than the target then perform binarySearch on mid+1 and r as left and right 
// else element not found

class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
        if(l>r)
            return -1;
        else {
            int mid = (l+r)/2;
            if(arr[mid]== x)
                return mid;
            else if(arr[mid]>x)
                return binarySearch(arr,0, mid-1,x);
            else if(arr[mid]<x) 
                return binarySearch(arr,mid+1,r,x);
            else 
                return -1;
        }
        
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
