//Problem 1: Binary Search

//   Time Complexity : The time complexity for this problem is O(log n) as we divide the list of elements by 2 until we reach the index.
//   Space Complexity : Space complexity would be O(1) as we did not use any extra memory aprt from input array
//   Any problem you faced while coding this : No

class BinarySearch {
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
        if(l<=r){
            int mid = (l + r)/2;
            if(arr[mid] == x)
                return mid;
            if(arr[mid] < x)
                return binarySearch(arr, mid + 1, r, x);
            else
                return binarySearch(arr, l, mid - 1, x);
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
