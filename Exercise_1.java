// Time Complexity : O(n/2 + constant) => O(n) 
// Space Complexity : O(1)
// Any problem you faced while coding this : None.

class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        // l = left side index
        // r = right side index
        // x = element being searched.

        // Find the middle index 
        if (r >= l) {
            int mid = l + (r - l) / 2;

            if (arr[mid] == x) return mid;
            
            // If key is on left side; smaller than mid
            if (arr[mid] > x) {
                // Recursive call
                return binarySearch(arr, l, mid - 1, x);
            }

            // Check right side of the mid
            // Recursive call
            return binarySearch(arr, mid + 1, r, x);

        }

        // If the element DNE in the array, return -1
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
