/* 
Time Complexity: O(Log n) 
Space Complexity: O(Log n)
*/

class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
         //Write your code here
         // repeat search till the right is greater than equal to left
        if (r >= l) {
            
        int mid = (l + r) / 2;

        // if element is found right at the mid of array return the index
        if (arr[mid] == x) {
            return mid;
        }

        //if element is less than arr[mid] then search in second half with r = mid - 1
        if (arr[mid] > x) {
            r = mid - 1;
            return binarySearch(arr, l, r, x);
        }

        //if element is greater than arr[mid] 
        if (arr[mid] < x) {
            l = mid + 1;
            return binarySearch(arr, l, r, x);
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
