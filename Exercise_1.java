/*******
Exercise_1 : Binary Search.

Time Complexity :                               O(log n)
Space Complexity :                              O(1)
Did this code successfully run on Leetcode :    No (704. Binary Search)
Any problem you faced while coding this :       No
*******/

class BinarySearch { 
    // Returns index of x if it is present in arr[left.. right], else return -1 
    int binarySearch(int arr[], int left, int right, int x) 
    {
        int mid;
        while (left <= right ){
            mid = ( left + right) / 2;
            // if middle element is x, return index
            if ( x == arr[mid] ){
                return mid;
            }
            // if middle element is greater than x, search on right side
            else if ( x < arr[mid] ){
                right = mid - 1;
            }
            // if middle element is less than x, search on left side
            else {
                left = mid + 1;
            }
        }
        // return -1 if element not found
        return -1; 
    } 
  
    // Driver method to test above 
    public static void main(String args[]) 
    { 
        BinarySearch ob = new BinarySearch(); 
        int arr[] = { 2, 3, 4, 10, 40 }; 
        int n = arr.length; 
        int x = 1; 
        int result = ob.binarySearch(arr, 0, n - 1, x); 
        if (result == -1) 
            System.out.println("Element not present"); 
        else
            System.out.println("Element found at index " + result); 
    } 
} 
