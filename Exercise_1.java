class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 

    /*
    Time Complexity: O(log(n))
    Space Complexity: O(1), since we are only considering 1 element at any given time.
    Did this code successfully run on Leetcode : NA
    Any problem you faced while coding this : No
    */
    int binarySearch(int arr[], int l, int r, int x) 
    { 
      int left = l, right = r;

      
      while(left <= right){
        int mid = left + (right - left)/2;

        if(arr[mid] == x){
          return mid;
        } else if (arr[mid] > x) {
          right = mid-1;
        } else {
          left = mid + 1;
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
