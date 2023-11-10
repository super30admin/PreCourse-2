/*
    Time Complexity = O(logN)
    Space Complexity = O(logN)
    Did this code successfully run on Leetcode : yes
 */

class BinarySearch {
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    {
        int idx = (l+r)/2;
        if(x == arr[idx]){
            return idx;
        }else if(x < arr[idx] && idx >= l && idx <= r){
            idx = binarySearch(arr, l, idx - 1, x);
            return idx;
        }else if(x > arr[idx] && idx >= l && idx <= r){
            idx = binarySearch(arr, idx+1, r, x);
            return idx;
        }
        return -1;
        //Write your code here
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
