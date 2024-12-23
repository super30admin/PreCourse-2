import java.util.Arrays;

class BinarySearch {
    // Returns index of x if it is present in arr[l.. r], else return -1
    // Time Complexity : O(NlogN) + O(logN) = O(NlogN) for unsorted array and O(logN) for sorted array
    // Space Complexity : O(1) no extra memory is used
    int binarySearch(int[] arr, int l, int r, int x)
    {
        // Since the question does not mention that arr is a sorted array, first sort the input array
        // Sorting using quick sort - O(NlogN)
        Arrays.sort(arr);
        while (l <= r) { // O(logN)
            int mid = l + (r - l) / 2;
            if (arr[mid] == x) {
                return mid;
            }
            if (arr[mid] < x) {
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
