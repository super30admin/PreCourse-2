class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    // Time Complexity : O(logN) -> at each iteration the array gets half 
    // Space Complexity : O(1) -> We took no extra space, only constant space
    // Did this code successfully run on Leetcode : Yes
    // Any problem you faced while coding this : No
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //ASSUMING the array is SORTED (otherwise we will sort first)
        //I am not covering sorting here
        //checking till left is less or equal to right
        while(r>=l)
        {
            //checking the middle element
            int mid = (l+r)/2;
            //checking if middle element is equal to x
            if(arr[mid] == x)
                return mid;
            //if x is greater than middle element then we move right side of middle element
            if(x>arr[mid])
                l = mid + 1;
            //if x is lesser than middle element then we move left side of middle element
            else if(arr[mid]>x)
                r = mid-1;
        }
        //if not found then we got out of the while loop without returning anything
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
