class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
        if(r>0) // to check if array is not empty
        {
            int m = (l+r)/2; // middle index in array
            if(arr[m]==x)
            {
                return m;
            }
            else if(arr[m]<x)
            {
                return binarySearch(arr,m+1,r,x);
            }
            else
            {
                return binarySearch(arr,l,m-1,x);
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
