// Time Complexity: O(n)
// Space Complexity: O(1)
// Time Complexity: O(log n)
// Space Compelxity: O(1)
class BinarySearch {
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
        while(l<=r){
            int mid = l + (r-l)/2;

            // check if element at mid index is equal to x
            if(arr[mid] == x) return mid;

            // if element at mid index is less than x
            if(arr[mid] < x) l = mid + 1;

            // if element at mid is greater than x;
            else r = mid - 1;
        }
        // If search element is not found in the list
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
