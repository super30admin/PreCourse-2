// Time Complexity :O(log n)
// Space Complexity : O(log n)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : No
class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
        if(r >= l){
            int mid = l + (r - l)/2;
            if(arr[mid] == x){ //if the middle element is the target number, return the index
                return mid;
            }
            else if(arr[mid] < x){
                return binarySearch( arr, mid + 1, r, x); // the target value lies on the right side of mid. So, the lower boundary changes to mid + 1
            }
            else{
                return binarySearch(arr, l , mid - 1, x); // the target value lies on the left side of mid. So, the higher boundary changes to mid - 1
            }
        }
        return -1; // if the element is not found
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
