package PreCourse_2;

//Binary search algorithm, time complexity is O(logn)
public class BinarySearch {
	    // Returns index of x if it is present in arr[l.. r], else return -1 
	    int binarySearch(int arr[], int l, int r, int x) 
	    { 
	        //Write your code here
	    	if(arr == null || arr.length == 0) return -1;
	    	int result = 0;
	    	int mid = 0;
	    	while(l<r) {
	    		mid = l + (r-l)/2;
	    		if(arr[mid] == x) {
	    			result = mid;
	    			return result;
	    		}
	    		else if(arr[mid]<x) {
	    			l = l+1;
	    		}
	    		else {
	    			r = r-1;
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
	        int x = 11; 
	        int result = ob.binarySearch(arr, 0, n - 1, x); 
	        if (result == -1) 
	            System.out.println("Element not present"); 
	        else
	            System.out.println("Element found at index " + result); 
	    } 
	} 
