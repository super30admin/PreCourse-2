//TIme Complexity -> O(log n) since we are dividing the search space into half everytime using "mid"
//Space Complexity -> O(1) since we use only iteration
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : No
// Your code here along with comments explaining your approach:
// Here we have consider the mid variable and divide the search inteval into half (mid=l+(r-l)/2) everytime rather than just trying to match each element with the target(x)
// If the target element is exactly at the middle we return the mid index
// Else if the mid element is less than the target element then we bring the left to (mid+1)th position and then we try to search in the right half of the array
// Else if the mid element is greater than the target we search in the left half of the array by bringing r to (mid-1)th position
// If the element is not found we return -1 at end





class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
        while(l<=r){
            int mid = l+(r-l)/2;
            if(arr[mid]==x)
                return mid;
            else if(arr[mid]<x)
                l=mid+1;
            else{
                r=mid-1;
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
