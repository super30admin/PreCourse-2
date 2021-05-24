/**
 *	Time Complexity : O(logn)
 *
 * 1. Binary search input array should be sorted
 * 2. If array size is zero return -1
 * 3. find mid element of array and compare with search element
 * 4. if greater search right tree otherwise search left tree
 */
class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
    	if(r >= l) {
    		int mid= (l+r)/2;
    		if(arr[mid]==x) {
    			return mid;
    		} else if(arr[mid]> x) {
    			return binarySearch(arr, l, mid-1, x);
    		}else {
    			return binarySearch(arr, mid+1, r, x);
    		}
    	}
    	return -1;
    } 
  
} 

public class Exercise_1{
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
