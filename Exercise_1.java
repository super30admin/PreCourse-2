// Time Complexity : O(log n)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : NA
// Any problem you faced while coding this : No
class BinarySearch {
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        int h = arr.length-1;

        while(l<=h) {
            int mid = l+(h-l)/2;
            if (arr[mid] == x)
                return mid;
            else if (arr[mid] < x){
                l = mid+1;
            } else {
                h = mid-1;
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
        int x = 3;
        int result = ob.binarySearch(arr, 0, n - 1, x); 
        if (result == -1) 
            System.out.println("Element not present"); 
        else
            System.out.println("Element found at index " + result); 
    } 
} 
