// Time Complexity : Worst case performance is O(log n)
// Space Complexity : O(1)
// Any problem you faced while coding this : No

class BinarySearch {
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        if(r >= l) {
            int mid = l + (r - l) / 2;
            // If the mid element is in middle
            if(arr[mid]==x)
                return mid;
            // If the element is smaller than mid then it can not be present in left subarray
            if(arr[mid] > x)
                return  binarySearch(arr, l, mid -1, x);
            // Otherwise the element can be present in right subarray
            return binarySearch(arr, mid+1, r, x);
        }
        // Element is not present in array
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
