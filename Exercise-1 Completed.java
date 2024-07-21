class BinarySearch { 
    // Returns index of x if it is present in arr[l..r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) { 
        // Base case: If the search range is valid
        if (r >= l) { 
            int mid = l + (r - l) / 2; // Calculate the middle index

            // If the element is present at the middle itself
            if (arr[mid] == x) 
                return mid; 

            // If the element is smaller than mid, then it can only be present in the left subarray
            if (arr[mid] > x) 
                return binarySearch(arr, l, mid - 1, x); 

            // Else the element can only be present in the right subarray
            return binarySearch(arr, mid + 1, r, x); 
        } 

        // Element is not present in array
        return -1; 
    } 
  
    // Driver method to test above 
    public static void main(String args[]) { 
        BinarySearch ob = new BinarySearch(); // Create an instance of BinarySearch
        int arr[] = { 2, 3, 4, 10, 40 }; // Define a sorted array
        int n = arr.length; // Get the length of the array
        int x = 10; // Element to be searched
        int result = ob.binarySearch(arr, 0, n - 1, x); // Perform binary search
        if (result == -1) 
            System.out.println("Element not present"); // Print if the element is not found
        else
            System.out.println("Element found at index " + result); // Print the index of the found element
    } 
} 
