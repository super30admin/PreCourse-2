class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    // Complexity Log(n)
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
        while(l <= r){
            int mid = l + (r-l)/2; //finding the middle element and search left if less than and right if greater than this
            if(x ==  arr[mid]){
                return mid;
            }
            else if(x > arr[mid]){
                l=mid+1;
            }
            else{
                r=mid-1;
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
