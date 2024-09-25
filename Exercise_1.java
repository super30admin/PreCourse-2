//package precourse2;
import java.util.Arrays;
class BinarySearch { 
    
	
	// Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
    	//Array need to be sorted for Binary Search
    	
    	int mid = (int) Math.floor((l + r)/2);
    	System.out.println(mid);
    	if(l >= r)
    		return -1;
    	
    	if(arr[mid] == x)
    		return mid;
    	
    	
    	if(arr[mid] > x) {
    		return binarySearch(arr,l,mid,x);
    	}else {
    		return binarySearch(arr,mid + 1,r,x);
    	}
    	
    } 
  
    // Driver method to test above 
    public static void main(String args[]) 
    { 
        BinarySearch ob = new BinarySearch(); 
        int arr[] = { 2, 3, 4, 10, 40 }; 
        int n = arr.length; 
        int x = 10; 
        
        //Assuming if array is not sorted may be not required
        Arrays.sort(arr);
        
        int result = ob.binarySearch(arr, 0, n - 1, x); 
        if (result == -1) 
            System.out.println("Element not present"); 
        else
            System.out.println("Element found at index " + result); 
    } 
} 
