// Time Complexity : O(log N) - for a given sorted array, we keep reducing the search space based 
//on comparison of middle index's element and the target value
// Space Complexity : O(1) - no extra space
// Did this code successfully run on Leetcode : N/A
// Any problem you faced while coding this : N/A since I've already studied the standard Binary Search algorithm 



class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
        while(l<=r)
        {
            int mid = l + (r-l)/2;
            if(x==arr[mid])
            {
                return mid;
            }
            else if (x < arr[mid])
            {
                r = mid-1;
            }
            else
            {
                l = mid+1;
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
