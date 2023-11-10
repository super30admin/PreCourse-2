class BinarySearch { 
   /*
   	Time complexity - O(log N) where N is the size of the input array "arr".
   	Space complexity - O(log N) for recursive binary search for storing variables in stack space. 
			   
   */
    public static void main(String[] args) {
		
		BinarySearch ob = new BinarySearch(); 
        int arr[] = { 2, 3, 4, 10, 40, 60 }; 
        int n = arr.length, x = 4; 
        int result = ob.binarySearch(arr, 0, n - 1, x); 
        if (result == -1) 
            System.out.println("Element not present"); 
        else
            System.out.println("Element found at index " + result); 
	}
	
	// Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
        if(l > r || l < 0 || r >= arr.length)
            return -1;
            
        int mid = (r - l) / 2 + l;
        
        if(arr[mid] == x)
            return mid;
        if(x > arr[mid])
            return binarySearch(arr, mid + 1, r, x);
        else
            return binarySearch(arr, l, mid, x);
    } 
} 
