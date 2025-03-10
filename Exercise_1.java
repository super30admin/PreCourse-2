// Time Complexity : O(log n) where n is the size of the array
// Space Complexity : O(1)
class BinarySearch {
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x)
    {
        //Write your code here
        int mid = 0;
        while(r >= l) {
            //calculate middle index
            mid = l+(r-l)/2;
            // found the element return the index
            if(arr[mid] == x) return mid;
            // if target element is bigger than the middle element, search on the right half
            if(arr[mid] < x)
                l = mid+1;
            // else search on the left half
            else
                r = mid-1;
        }

        return -1; //Element not present
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
