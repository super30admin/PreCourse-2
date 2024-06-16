// Time Complexity : O(logn) where n is length of array
// Space Complexity : O(1) We are not creating any extra variables other than mid
// Did this code successfully run on Leetcode :
// Any problem you faced while coding this :

class BinarySearch {
    // Returns index of x if it is present in arr[l.. r], else return -1
    int binarySearch(int arr[], int l, int r, int x)
    {
        //Write your code here
      while(l<=r) {
        int mid = (r + l) / 2; //Calculate mid index, helps to locate target
//        System.out.println(mid);
        if (arr[mid] == x)
          return mid;  //if value at mid index matches target, return mid index
        else if (arr[mid] < x) {
          l = mid+1;  //if mid value is less than target, move left pointer to mid+1. Since all the elements before mid+1 will be smaller than target
          binarySearch(arr, l, r, x);
        } else {
          r = mid-1; //if mid value is greater than target, move right pointer to mid-1. Since all the elements next to mid-1 will be greater than target
          binarySearch(arr, l, r, x);
        }
      }
      return -1;  //Reaches this point when search is complete i.e left and right pointers cross each other but nothing is returned. Target not found
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
