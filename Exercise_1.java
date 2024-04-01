// Time Complexity : O(log N)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : yes
// Any problem you faced while coding this : none


// Your code here along with comments explaining your approach
//Used a loop to run from start till and and checking every mid for the target.
class BinarySearch { 
  
  
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
      // Returns index of x if it is present in arr[l.. r], else return -1 
    public int binarySearch(int[] arr, int start, int end, int target){
        while(start<=end){
            int mid = start+(end-start)/2;

            if(arr[mid]==target){
                return mid;
            }

            if(arr[mid]< target){
                start = mid+1;
            }
            else {
                end = mid-1;
            }
 
        }
        return -1;
    }
} 
