// Time Complexity : O(logN)  as N/2^k = 1
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : ran it successfully on local machine
// Any problem you faced while coding this : Had to read about the steps of the algo and also about recursion

/*Divide the array around middle element and check whether the element to be searched is the middle element or is in left
or is in the right array and then repeat this recursively till the array cannot be divided further*/ 
// Your code here along with comments explaining your approach

class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        if(l>r){
            return -1;
        }
        //Write your code here
        int mid = (l + r)/2;
        if(x==arr[mid]){
            return mid;
        }else if(x<arr[mid]){
            return binarySearch(arr, l, mid-1, x);
        }else if(x>arr[mid]){
            return binarySearch(arr, mid+1, r, x);
        }else{
            return -1;
        }

    } 
  
    // Driver method to test above 
    public static void main(String args[]) 
    { 
        BinarySearch ob = new BinarySearch(); 
        int arr[] = { 2, 3, 4, 10, 40 }; 
        int n = arr.length; 
        int x = 4; 
        int result = ob.binarySearch(arr, 0, n - 1, x); 
        if (result == -1) 
            System.out.println("Element not present"); 
        else
            System.out.println("Element found at index " + result); 
    } 
} 
