// Time Complexity : O(log(n))
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : no


// Your code here along with comments explaining your approach
/*
Binary search algorithm is applied on a sorted array to find out the index of the given element if present in
the given array, so as we know the array is sorted, so based on the value of mid element, we estimate the location
of the given target element, and based on that we move our left (l) and right (r) pointers to search for the element
in the half array
 */
class BinarySearch {
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
        while(l<r){
            int mid = l + (r-l)/2;

            if(arr[mid] == x){
                return mid;
            }else if(arr[mid] > x){
                r = mid-1;
            }else{
                l = mid+1;
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
