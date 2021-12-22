// Time Complexity : O (log n)
// Space Complexity : O (log n)
// Did this code successfully run on Leetcode : Ran it on VS Code. 
// Any problem you faced while coding this : No

// Your code here along with comments explaining your approach
// Check if l is greater than r if not calcualate the mid index and check for the value at mid index in the
// array if it matches the given integer value return the mid index. Otherwise check if given integer value is
// greater than value at mid index in array, if yes make a recursive binary search call by updating the value
// of l with mid+1. Check if given integer value is less than value at mid index in array, if yes make a 
// recursive binary search call by updating the value of r with mid-1. If we encounter value of l greater 
// than r then it means we ran over the entire array and didnot find the given integer, then we return -1

class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
        if(l>r){
            return -1;
        }
        int mid = Math.floorDiv(l+r,2);
        if(arr[mid]==x){
            return mid;
        }
        else if(arr[mid]>x){
            return binarySearch(arr, l, mid-1, x);
        }
        else{
            return binarySearch(arr, mid+1, r, x);
        }
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
