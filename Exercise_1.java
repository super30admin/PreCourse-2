/*
since we increment two counters from either side it takes half the time so Time complexity log n for search
Since it is constant space it is O(1) space
*/
class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
		while(l<r) {
    		if(arr[l]==x) {
    			return l;
    		}
    		l++;
    		if(arr[r]==x) {
    			return r;
    		}
    		r--;
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
