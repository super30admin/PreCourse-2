// Time Complexity : O(log(N))
// Space Complexity : O(1)
// Did this code successfully run on Leetcode :
// Any problem you faced while coding this : No


class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
        int index = -1;    //default index is -1 as it represents that element is not found.
        while(l <= r){
            int mid = (l+r)/2;   //searching only the satisfied space as the array is sorted.
            if(arr[mid] == x){
                index = mid;
                break;
            }
            else if(arr[mid] < x){
                l = mid+1;
            }
            else{
                r = mid-1;
            }
        }
        return index;
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
