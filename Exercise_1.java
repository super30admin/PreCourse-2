package precourse2;
//Time Complexity : O(log n)
//Space Complexity : O(1)
//Did this code successfully run on Leetcode : Yes
//Any problem you faced while coding this : No

//Your code here along with comments explaining your approach

class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    {
    	//Write your code here
    	int mid=0;	
    	while(l<r) {
    		mid=l+(r-l)/2;	
    		if(arr[mid]==x)	return mid;		//returns the index when the target matches the value at current index
    		if(arr[mid]<x) {	//update value of left to mid+1 to skip the elements less than target
    			l=mid+1;
    		}else {				//update value of right to mid to skip the elements greater than target
    			r=mid;
    		}
    	}
		return -1; 
    }
} 
// Driver method to test above 
class Exercise_1{
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