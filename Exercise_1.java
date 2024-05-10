//Time Complexity: O(log N)
//Space Complexity: O(1)
// Did this code successfully run on Leetcode : YES
// Any problem you faced while coding this : NO
class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
        while( l <= r){
            //Calculate middle
            int m = (l + r) / 2;
            //Check if x is present at mid then return
            if(arr[m] == x)
            return m;
            //Check if x is greater than middle then we check in the upper half of the array. 
            if(arr[m] < x){
                l = m + 1;
            }
             //Check if x is lesser than middle then we check in the lower half of the array. 
            else{
                r = m - 1;
            }
        }
        // if elemeent is not present
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
