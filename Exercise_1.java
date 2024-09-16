// Time Complexity : O(log n)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : None
// Your code here along with comments explaining your approach

class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
        int mid = (l + (r - l)/2); // To avoid numbers exceeding int range, calculated mid value of the array using this approach
        
        while(l<=r) // checking each time if left pointer should not cross the right one
        {
          mid = (l + (r - l)/2); // calculating mid value of array for each split
            if(arr[mid]==x) // if value found
                return mid; // return index at which value was found i.e mid
            else if(arr[mid]>x) // if value at mid greater than that to be found
                r = mid-1; // value should be present in the lower half
            else
                l = mid+1; // else value would be present in upper half
        }
   return -1;  // returning -1 if element not found

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
