// Time Complexity : o(log(n))
// Space Complexity : o(log(n)) due to use of stack for recursion
// Did this code successfully run on Leetcode :
// Any problem you faced while coding this :

class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        if(l <= r) {
        		int mid = (l + r)/2;
        		
        		if(arr[mid] == x)
        			return mid;
        		
        		if(x < arr[mid])
        			return binarySearch(arr, l, mid - 1, x);
        		else
        			return binarySearch(arr, mid + 1, r, x);
        		
        } else
        		return -1;
    }
    
    int binarySearchItr(int arr[], int l, int r, int x) 
    { 
        while(l <= r) {
        		int mid = (l + r)/2;
        		
        		if(arr[mid] == x)
        			return mid;
        		
        		if(l == r)
        			break;
        		
        		if(x < arr[mid])
        			 r = mid - 1;
        		else
        			 l = mid + 1;
        		
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
        int result = ob.binarySearchItr(arr, 0, n - 1, x); 
        if (result == -1) 
            System.out.println("Element not present"); 
        else
            System.out.println("Element found at index " + result); 
    } 
} 
