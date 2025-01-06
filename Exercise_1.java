class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        int low = l;
        int high = r;
        int mid = low + (high -low)/2;
        if(arr[mid] == x)
        {
            return arr[mid];
        }
        else
        {
            if(arr[mid] > x) {
                high = mid -1;
                return binarySearch(arr, low, high, x);
            }
            else if(arr[mid] < x)    {
                low = mid +1;
                return binarySearch(arr, low, high, x)
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
        int x = 10; 
        int result = ob.binarySearch(arr, 0, n - 1, x); 
        if (result == -1) 
            System.out.println("Element not present"); 
        else
            System.out.println("Element found at index " + result); 
    } 
} 
