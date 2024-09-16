// Time Complexity : O(n)
// Space Complexity : O(Log n)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : I don't understand how to calculate time and space complexities :(

class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
        if(r >= 1){
            int mid = l + (r - 1) / 2;

            //if element is at the middle index
            if(arr[mid] == x){
                return mid;
            }
            //if element is on the left of the middle index (smaller)
            if(arr[mid] > x){
                return binarySearch(arr, l, mid - 1, x);
            }
            //if element is on the right of the middle element (bigger)
            return binarySearch(arr, mid + 1, r, x);
        }
        //element is not present
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
