// Time Complexity : O(log n)
// Space Complexity : O(1)

// Your code here along with comments explaining your approach
/*
* Pseudo code: use while loop to iterate over sub arrays
* each iteration make a decision to go right or left array
* by resetting l and r values to mid+1 or mid -1
* depending of idf condition check for target value greater or smalled
*
* */


public class BinarySearch {
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    {
        /*while l and r don't cross each other keep running*/
        while (l <= r) {
            //r-l prevents integer overflow
            int m = l + (r - l) / 2;
            if (arr[m] == x)
                return m;
            //if m is < x go right side array
            if (arr[m] < x)
                l = m + 1;
            else
                //if m is > x go left side array
                r = m - 1;
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
