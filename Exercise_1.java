/*
Time Complexity : O(log n) since everything is done after traversing the entire arraylist.
Space Complexity : O(n) since we create memory when array is generated

Did this code successfully run on Leetcode :
Finished in 68 ms
Element found at index 5

Any problem you faced while coding this :
None.

Your code here along with comments explaining your approach :
Straight forward approach.
*/

class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    public int binarySearch(int[] arr, int l, int r, int x) 
    { 
        if(l<r){
            int mid = (l + r )/2;
            if( arr[mid] == x)
                return mid+1;
            if(arr[mid]>x){
                return binarySearch(arr, l, mid, x);
            } else {
                return binarySearch(arr, mid + 1, r, x);
            }
        } else if (l == r){
            if( arr[l] == x)
                return l+1;
            return -1;
        } else {
            return -1;
        }
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
