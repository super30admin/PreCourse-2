// Time Complexity : O(Log n)
// Space Complexity : O(1)

// Did this code successfully run on Leetcode : n/a
// Any problem you faced while coding this : No


// Your code here along with comments explaining your approach
/*
Check for left and right indices that left <= right

Find mid point of left and right: If element at mid point = x return that mid point(index)
If element at mid point < x => X is located in the right side of mid point
If element at mid point > x => X is located in the left side of mid point

If element not found then simply return -1

*/



class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
        while(l <= r){
            int mid = (l + r) / 2;

            if(arr[mid] == x){
                return mid;
            }
            else if(arr[mid] < x){
                l = mid + 1;
            }
            else{
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
