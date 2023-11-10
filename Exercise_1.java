/**
 * Space complexity : O(1)
 * Time complexity: O(log n)
 * Did this code successfully run on Leetcode : Yes
 * Any problem you faced while coding this : Finding complexity
 */
class BinarySearch {
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
        //This loop will break if the left index is greater than right index
        //indicating that the element is not found in the array
        //And -1 is returned
        while(l <= r){
            //Mid is used to divide the array into half
            int mid = (l + r)/2;
            //if target element equals the element at middle index
            // then we can stop further processing and return mid
            if(x == arr[mid])
                return mid;
            //if target element is less than the element at middle index
            // then we process the left half of the array
            else if(x < arr[mid])
                r = mid - 1;
            //if target element is greater than the element at middle index
            // then we process the right half of the array
            else
                l = mid + 1;
        }
        //If the element is not found in the array
        //then the control reaches here, and we return -1
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
