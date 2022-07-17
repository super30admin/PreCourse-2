// Online Java Compiler
// Use this editor to write, compile and run your Java code online

/*
 * 
 * 
 * // Time Complexity : O(logn)
// Space Complexity : 1
// Did this code successfully run on Leetcode : yes
// Any problem you faced while coding this :


// Your code here along with comments explaining your approach

 * 
 * */

class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
    	
 
        while(l<=r){
        	//calculate mid of the array
        int mid = l + (r - l) / 2;
        if(arr[mid]==x)   		    //if mid is equal to target then return mid
            return mid;
        else if(x>arr[mid])    // if target is greater than mid value then change low = mid+1;
            l = mid+1;
        else
            r= mid-1;  //if target is less than mid value then change high = mid =1;
        }
        return -1; //return -1 if element is not found
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