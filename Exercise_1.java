
// Time Complexity : O(log n)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : yes
// Any problem you faced while coding this :


// Your code here along with comments explaining your approach

class BinarySearch {
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x)
    {
        //Write your code here
        while(l<=r) {
            int mid = l + ((r-l)/2); //find midpoint, if target - arr[mid] then return mid else adjust left, right values based on target val
            if(arr[mid] == x)
                return mid;
            else if(arr[mid]<x) {
                l = mid + 1;
            } else {
                r = mid - 1 ;
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
        System.out.println(result);
        if (result == -1)
            System.out.println("Element not present");
        else
            System.out.println("Element found at index " + result);
    }
} 