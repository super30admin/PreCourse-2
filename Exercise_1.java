//Time complexity : O(log N)
//Space Complexity : O(1)
class BinarySearch {
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
        while(l <= r) {
            int mid = l + (r-l)/2;

            //check if x is equal to element at mid index
            if(arr[mid] == x)
                return mid;
            //if element at mid index is less than x, then shift l to mid+1
            else if(arr[mid] < x)
                l = mid+1;
            //if element at mid index is less than x, then shift r to mid-1
            else
                r = mid-1;
        }

        //return -1 if the target element is not found in the array
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
