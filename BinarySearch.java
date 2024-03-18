class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
        
        while(l < r) {
            int mid = (l + r) / 2;
            if(arr[mid] == x)   return mid;
            if(arr[mid] > x) r = mid-1;
            else l = mid + 1;
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
        int result2 = ob.binarySearch(arr, 0, n - 1, 2);
        int result3 = ob.binarySearch(arr, 0, n - 1, 50);
        if (result == -1) 
            System.out.println("Element 10 not present"); 
        else
            System.out.println("Element 10 found at index " + result); 

        if (result2 == -1) 
            System.out.println("Element 2 not present"); 
        else
            System.out.println("Element 2 found at index " + result2); 

        if (result3 == -1) 
            System.out.println("Element 50 not present"); 
        else
            System.out.println("Element 50 found at index " + result3); 
    } 
} 
