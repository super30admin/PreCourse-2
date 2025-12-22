import java.util.Arrays;

//Time: O(log n) for search.
//Space: O(1)
class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) { 
        //Write your code here
        //Rules of binary search are 1. array should be sorted, 2. we repeatedly check the middle element

        if(arr == null || arr.length == 0) 
            return -1;
        
        Arrays.sort(arr);

        while(l <= r) {
            int mid = l+ (r -l) /2;
            if (arr[mid] == x) {
                return mid;
            } else if (arr[mid] < x) {
                l = mid + 1;
            } else {
                r = mid -1;
            }
        } 

        return -1;
    } 
  
    // Driver method to test above 
    public static void main(String args[]) 
    { 
        BinarySearch ob = new BinarySearch(); 
        int arr[] = { 5, 3, 19, 30, 1 }; 
        int n = arr.length; 
        int x = 3; 
        int result = ob.binarySearch(arr, 0, n - 1, x); 
        if (result == -1) 
            System.out.println("Element not present"); 
        else
            System.out.println("Element found at index " + result); 
    } 
} 
