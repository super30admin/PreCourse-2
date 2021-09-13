// Time Complexity : O(log(n))
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : c

// Your code here along with comments explaining your approach

class BinarySearch {
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
        // we have two pointers left and right, we first find the middle element and check if it is equal to the value we want to search for if it is then we return the index
        // if it doesn't matches middle element then we check if middle element is less than x or greater than x and we update left/right pointer accordingly such that we are in search space of x
            while(l<=r) {
                int mid = l + (r - l) / 2;
                if (arr[mid] == x)
                    return mid;
                else if (arr[mid] > x)
                    r = mid - 1;
                else
                    l = mid + 1;
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
