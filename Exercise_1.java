/*
** Time Complexity - O(logn) 
** Space Complexity - O(logn)
** Did this code successfully run on Leetcode : yes
** Any problem you faced while coding this : No
*/


class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    {
        //Write your code here
        if(r >= l) {
            //divide the given array in to two
            int mid = l + (h – l)/2;

            System.out.println("mid : " + mid);
            //if mid element matches to key then return the element
            if(arr[mid] == x) {
                return mid;
            }
            //recursive call to search for the element
            if(arr[mid] < x) {
                //if the element is greater than mid, then search for an element in right sub array
                return binarySearch(arr, mid+1, r, x);
            } else {
                //if the element is smaller than mid then search in left sub array
                return binarySearch(arr, l,mid-1, x);
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
