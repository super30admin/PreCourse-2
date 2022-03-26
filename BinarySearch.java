package precourse2;
//space complexity: O(log(n))
//time complexity: O(log(n))
class BinarySearch { 
    // Returns index of element if it is present in arr[start.. end], else return -1 
    int binarySearch(int arr[], int start, int end, int element) 
    {
    	if (end >= start) {
            int mid = start + (end - start) / 2;
            if (arr[mid] == element) {
            	 return mid;
            }     
            if (arr[mid] > element) {
	             return binarySearch(arr, start, mid - 1, element);
            }
            return binarySearch(arr, mid + 1, end, element);
    	}
    	return -1;
    } 
  
    // Driver method to test above 
    public static void main(String args[]) 
    { 
        BinarySearch ob = new BinarySearch(); 
        int arr[] = { 2, 3, 4, 10, 40 }; 
        int n = arr.length; 
        int x = 10; //search value
        int result = ob.binarySearch(arr, 0, n - 1, x); 
        if (result == -1) 
            System.out.println("Element not present"); 
        else
            System.out.println("Element found at index " + result); 
    } 
} 
