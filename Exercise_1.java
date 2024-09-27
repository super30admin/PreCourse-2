// Time Complexity : O(logN)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode :
// Any problem you faced while coding this :No

class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //if left pointer is less than or is equal to right pointer then elements might be present in the array else return -1;
        if(l <= r){
            int mid = l + (r-l)/2; //calculate mid
            
            if( arr[mid] == x){ // if the search element is at mid, return mid
                return mid;
            }
            if( arr[mid] < x){ // if search element is less then change the left pointer
                return binarySearch(arr, mid+1, r, x);
            }
            else{ // if search element is greater then change the right pointer
                return binarySearch(arr, l, mid-1, x);
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