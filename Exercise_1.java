//after googling found out what binary tree search was and how we have to keep halving the array until we find the number
class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) { 
        //Write your code here
    	int INDEX = -1;
    	for (int i = l; i < r; i++ ) {    		
    		if (arr[i] == x) {
    			INDEX = i;
    		}     			
    	}    	
    	return INDEX;
    } 
  
    // Driver method to test above 
    public static void main(String args[]) { 
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
