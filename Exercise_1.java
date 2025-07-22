class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    // time complexity: O(log(n))
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
        while(l<r){
        int mid = (l+r)/2 ; // find mid element
        if(arr[mid]==x){
            return mid;
        }
        else if(x>arr[mid]) // search in right side array
        {
           l = mid+1;
        }
        else // search in left side array
        {
            r = mid-1;
        }
        }
        return -1;
    } 
  
    // Driver method to test above 
    // Time Complexity: O(log(n))
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
