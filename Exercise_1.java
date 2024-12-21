// Time Complexity :O(logN) (Actually learned this value).
// Space Complexity : O(1) no extra space being used.
// Did this code successfully run on Leetcode : YES(Over local ide)..
// Any problem you faced while coding this : None, other than t.c and s.c.
class BinarySearch {
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
        //Loop until the left index if reaches to the right index.
        while(l<=r){
            //carry out the mid between the left and right index so all the elements left to mid are small and right to mid are larger.
            int mid = l+(r-l)/2;
            //check if the recently found mid-index has the value we're looking for.
            //If not check if the value to be found is greater than or less than mid and change left and right accordingly.
            //Basically we're reducing the search space for the value to be found by half everytime.
            if(x == arr[mid]) return mid;
            else if(arr[mid] > x){
                r = mid - 1;
            }
            else{
                l = mid + 1;
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
        int x = 400;
        int result = ob.binarySearch(arr, 0, n - 1, x); 
        if (result == -1) 
            System.out.println("Element not present"); 
        else
            System.out.println("Element found at index " + result); 
    } 
} 
