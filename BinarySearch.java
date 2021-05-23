// Time Complexity : O(logn)
// Space Complexity : O(n) for n elements
// Did this code successfully run on Leetcode :
// Any problem you faced while coding this :

public class BinarySearch {
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        int mid;
        while(l<=r){
            mid = (l+r)/2;
            if(arr[mid]==x){
                return mid;
            } else if(arr[mid]<x){
                l=mid+1;
            } else
                r=mid ;
        }
        return -1;
    } 
  
    // Driver method to test above 
    public static void main(String args[]) 
    { 
        BinarySearch ob = new BinarySearch(); 
        int arr[] = { 2, 3, 4, 10, 40 }; 
        int n = arr.length; 
        int x = 40;
        int result = ob.binarySearch(arr, 0, n - 1, x); 
        if (result == -1) 
            System.out.println("Element not present"); 
        else
            System.out.println("Element found at index " + result); 
    } 
} 
