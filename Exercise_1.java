// Time Complexity : O(logN)  as N/2^k = 1
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : ran it on local machine
// Any problem you faced while coding this : No
class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
        while(l<=r){
            int mid = l + (r-l)/2;
            if(arr[mid] == x){
                return mid;
            }
            if(arr[mid] > x){
                r=mid-1;
            }
            else if(arr[mid] < x){
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
        int x = 2; 
        int result = ob.binarySearch(arr, 0, n - 1, x); 
        if (result == -1) 
            System.out.println("Element not present"); 
        else
            System.out.println("Element found at index " + result); 
    } 
} 
