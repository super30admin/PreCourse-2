class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Time Complexity - O(log N) where N is the length of the array

        //In Binary Search algorithm, as the array is always sorted, we first find the mid-point of the array and compare it
        // with the required element. If the required element equals the mid element, we return the index. Else,
        //if the element is less than mid, we perform serach in left part otherwise we perform serach in right part 

        while(l <= r)
        {
            int mid = l + (r-l)/2 ;
            if(arr[mid] == x)
                return mid;
            else if(arr[mid] > x)
                r--;
            else if(arr[mid] < x)
                l++;          
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
