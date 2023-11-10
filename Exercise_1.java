// Time Complexity : O(log n) 
// Space Complexity : O(1) 
// Did this code successfully run on Leetcode : Yes  https://leetcode.com/problems/binary-search/description/
// Any problem you faced while coding this:  No
// Your code here along with comments explaining your approach: Here I have used the iterative method. I have set the index of the middle element as mid.  If the target value(in this case x) <arr[mid], then we will change the highest index(in this case r) to mid-1 else m+1. We keep repeating this until value at mid==target. If we don’t find the value in any of the elements, then we return -1. 

class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
        while (l<=r)
        {
            int mid=l+(r-l)/2;
            if(arr[mid]==x)
            {
                return mid;
            }

            else if(x<arr[mid])
            {
                r=mid-1;
            }

            else
            {
                l=mid+1;
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
