/*
 Time complexity: O(logN) where N is size of array. Assumption made that the array is sorted in ascending order
 Scpace complexity: O(1)
 Did this code successfully run on Leetcode : Yesß
 Any problem you faced while coding this : No
*/

class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
        int idx = -1;
        if(arr == null || arr.length == 0){
            return idx;
        }

        while(l <= r){
            int mid = l  + (r - l)/2;
            if(arr[mid] == x){
                return mid;
            }else if(x < arr[mid]){
                r = mid - 1;
            }else{
                l = mid + 1;
            }
        }

        return idx;
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
