// Time Complexity :O(log n)
// Space Complexity : O(n)  n-length of the array. 
// Did this code successfully run on Leetcode : N/A
// Any problem you faced while coding this : Mid element formula


// Your code here along with comments explaining your approach
class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
		//Write your code here
	    if(r>=l) // right index should always be greater than left index
		{
		int mid=l+(r-l)/2; //r-l gives the number of elements between l and r. (r-l)/2 gives the median. l+(r-l)/2 gives index
		if(arr[mid]==x)
			return mid;
		else if(arr[mid]>x)
			return binarySearch(arr,l,mid-1,x);
		else
			return binarySearch(arr,mid+1,r,x);
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
