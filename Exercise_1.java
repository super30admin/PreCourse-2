/* Algorithm: Binary Search
 * Binary search divides the given space into half and tries to find the target.
 * 1. Find mid of the space ==> (left + right)/2 or to avoid overflow (left + (right-left))/2
 * 2. Search until no more space to divide (left <= right)
 * 3. If target is less than mid value ==> right = mid-1
 * 4. Else if target is greater than mid value ==> left = mid+1
 * 5. Else return -1 ==> Target not found
 * 
 * Time Complexity: O(log N)
 * Space Complexity: O(1)
*/
class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int left, int right, int target) 
    { 
        if(arr == null || arr.length == 0)
        {
            return -1;
        }
        
        while(left <= right)
        {
            int mid = left + (right - left)/2;
            
            if(target == arr[mid])
            {
                System.out.println("Found Target!");
                return mid; 
            }
            else if(target < arr[mid])
            {
                right = mid-1;
            }
            else
            {
                left = mid+1;
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
