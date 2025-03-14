// Time Complexity : O(log n to the base 2) -> O(log n)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode: N/A
// Any problem you faced while coding this: Nope


// Your code here along with comments explaining your approach
class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        while(l <= r) {
            // To avoid Integer overflow
            int mid = l + (r - l) / 2;
            // Check if mid is equal to x if yes then return mid
            // if the mid number is less than desired number then change the left to mid + 1 otherwise update right to mid - 1
            if(arr[mid] == x) {
                return mid;
            } else if(arr[mid] < x) {
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        
        return -1;
    } 
  
    // Driver method to test above 
    public static void main(String args[]) 
    {   
        // Some Analysis
        BinarySearch ob = new BinarySearch();
        // Here the length of array is 5
        // So log 5 to base 2 would mean while loop would run max 2 or 3 times. Since log5 to base 2 would be 2.32
        // So if array length is 1024 it would only take 10 iterations to find item
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
