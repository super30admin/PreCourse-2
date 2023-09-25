// Time Complexity : O(log n) 
// Space Complexity : O(log n) 
// Did this code successfully run on Leetcode : -
// Any problem you faced while coding this : -

class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
    	/*	Assumption: the input array would always be sorted as that is a pre-requisite for binary search tree
    	 *	If array is not empty, while first index is less or equals to right index identify the mid index,.
    	 *		If value at mid index equals the value that we are searching, return value at mid index
    	 *		else if value that we are searching is less than value at mid index, we move to the left sub-tree
    	 *		else if value that we are searching is greater than value at mid index, we move to the right sub-tree
    	 *	and if value that we are searching for is not present we return -1
    	 * */
    	if(arr.length > 0) {
    		while (l<=r) {
    			int mid = (l+r)/2;    			
    			if(arr[mid] == x) {
    				return mid;
    			}
    			else if(x < arr[mid]) {
    				r = mid-1;
    			}
    			else {
    				l = mid+1;
    			}
    		}
    		return -1;
    	}
    	else {
    		System.out.println("Empty Array");
    		return -1;
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
        
        //Input is an array of length 1 - ele is present
        int arr2[] = { 10 }; 
        int n2 = arr2.length; 
        int x2 = 10; 
        int result2 = ob.binarySearch(arr2, 0, n2 - 1, x2); 
        if (result2 == -1) 
            System.out.println("Element not present"); 
        else
            System.out.println("Element found at index " + result2);
        
        //Input is an array of length 1 - ele is not present
        int arr3[] = { 1 }; 
        int n3 = arr3.length; 
        int x3 = 10; 
        int result3 = ob.binarySearch(arr3, 0, n3 - 1, x3); 
        if (result3 == -1) 
            System.out.println("Element not present"); 
        else
            System.out.println("Element found at index " + result3);
        
        //Input is an array of length 2 - ele is present
        int arr4[] = { 1, 10 }; 
        int n4 = arr4.length; 
        int x4 = 10; 
        int result4 = ob.binarySearch(arr4, 0, n4 - 1, x4); 
        if (result4 == -1) 
            System.out.println("Element not present"); 
        else
            System.out.println("Element found at index " + result4);
        
        //Input is an array of length 2 - ele is not present
        int arr5[] = { 1, 5 }; 
        int n5 = arr5.length; 
        int x5 = 10; 
        int result5 = ob.binarySearch(arr5, 0, n5 - 1, x5); 
        if (result5 == -1) 
            System.out.println("Element not present"); 
        else
            System.out.println("Element found at index " + result5);
        
        //Input is an empty array
        int arr6[] = {}; 
        int n6 = arr5.length; 
        int x6 = 10; 
        int result6 = ob.binarySearch(arr6, 0, n6 - 1, x6); 
        if (result6 == -1) 
            System.out.println("Element not present"); 
        else
            System.out.println("Element found at index " + result6);
                
    } 
} 
