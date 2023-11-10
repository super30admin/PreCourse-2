//time complexity: O(log h)as we are dividing array in half after every iteration, h is the height of tree
//space complexity: O(log h) h is the height of tree
// successfully executed

class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        
    	int index = 0;
        while(r>=l) {
        	int mid = (l+r)/2;
        if(x==arr[mid]) {
        	 index= mid;
        	return index;
        }
        else if (x>arr[mid]) {
        	l= mid+1;
		}
        else {
        	r=mid-1;
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
        int x = 60; 
        int result = ob.binarySearch(arr, 0, n - 1, x); 
        if (result == -1) 
            System.out.println("Element not present"); 
        else
            System.out.println("Element found at index " + result); 
    } 
} 
