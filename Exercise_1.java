class BinarySearch {
    /**
     * Returns index of x if it is present in arr[l.. r], else return -1
     * @param arr integer array
     * @param l left index in array
     * @param r right index in array
     * @param x x is  value to be serched in array
     * @return integer index of the value x if present in an array else -1
     */
    //Time complexity:log(n) where n is array size
    //Space complexity is:o(1) as I am only using constant space irrespective of my input size.
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        while(l<=r){
            int mid=(l+r)/2;
            if(arr[mid]==x){
                return mid;
            }
            else if(x<arr[mid]){
                r=mid-1;
            }
            else{
                l=mid+1;
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
        int x = 0;
        int result = ob.binarySearch(arr, 0, n - 1, x);
        if (result == -1) 
            System.out.println("Element "+ x +" not present in an array");
        else
            System.out.println("Element "+ x +" found at index " + result);

        x=10;
         result = ob.binarySearch(arr, 0, n - 1, x);
        if (result == -1)
            System.out.println("Element "+ x +" not present in an array");
        else
            System.out.println("Element "+ x +" found at index " + result);
    } 
} 
