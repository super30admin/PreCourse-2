// Time Complexity : O(log n)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : Yes

class BinarySearch {
    //  Returns index of x if it is present in arr[l.. r], else return -1
    int binarySearch(int arr[], int l, int r, int x) 
    {
        while (l <= r) {
            //  Find middle index of the array
            int m = (l+r)/2;

            //  Check if element exists at the middle index
            if (arr[m] == x) {
                return m;
            }
            else {
                //  If element is less than the one found at the middle index, search only in the array's first half
                if (x < arr[m]) {
                    r = m - 1;
                }
                //  If element is greater than the one found at the middle index, search only in the array's second half
                else {
                    l = m + 1;
                }
            }
        }

        return -1;  //  element not found
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
