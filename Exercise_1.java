// Time Complexity : O(log N)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : 
// Any problem you faced while coding this : No


// Your code here along with comments explaining your approach
//1. first calculate the mid and then compare the given number x with two sub arrays
//2. if number x is larger then mid value, update l left as mid+1 (right sub array)
//3. if number x is smaller than mid value, update r right as mid-1 (left sub array)

class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
        while(r >= l){
            int mid = l+(r-1)/2;
            if(arr[mid] == x){
                return mid;
            }
            else if(x < arr[mid]){
                r = mid;
            }
            else {
                l = mid;
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
