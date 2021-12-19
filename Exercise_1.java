// Time Complexity : O(1)
// Space Complexity : O(log n)
// Did this code successfully run on Leetcode : NA
// Any problem you faced while coding this : No


// Your code here along with comments explaining your approach


class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
		//initialize start and end
		int start=l;
		int end=r;
		
		//loop to check through the array
		while(start<=end) {
			int mid=(start+end)/2;
		if(arr[mid]==x) {
            //return index on finding the element
			return mid;
		}else if(x>arr[mid]) {
			start=mid+1;
			
		}else if(x<arr[mid]) {
			end=mid-1;
		}
		
		}
		//return -1 if loop is passed
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
