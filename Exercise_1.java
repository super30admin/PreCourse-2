// Time Complexity : O(log n)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode :
// Any problem you faced while coding this : NO

class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Calculating midIndex for given index range
        int midIndex = l + ((r-l) /2 );

        //If left index is greater than right index or left index is less than zero, return -1
        if(l > r || l < 0)
            return -1;
        // If midIndex value is equal to target value, return midIndex
        else if(arr[midIndex] == x)
            return midIndex;
        // If midIndex value is greater than target value, then search in left subarray of midIndex
        else if(arr[midIndex] > x)
            return binarySearch(arr, l, r-midIndex -1, x);
        // If midIndex value is less than target value, then search in right subarray of midIndex
        else if(arr[midIndex] < x)
            return binarySearch(arr, l + midIndex -1, r, x);
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
