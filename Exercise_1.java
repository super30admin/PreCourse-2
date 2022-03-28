// best case O(1) else O(logn)
class BinarySearch {
    // Returns index of x if it is present in arr[l.. r], else return -1
    // It is a recursive algorithm with time and space complexity O(logn)
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        if (r>=l){  //checking if array has at least 1 element
            int mid = (l+r)/2;  // Finding mid index of array
            if(arr[mid]==x){    //Checking if that mid index has the element we need
                return mid;
            }else                // If not then checking if that is present in the first half of the array or second half.
            if(x<arr[mid]){       // and then returning and calling the method
                return binarySearch(arr, l, mid-1, x);   //again with the first half elements or second half accordingly
            }
                else if(x>arr[mid]){
                    return binarySearch(arr, mid+1, r, x);}
        }
    return -1; }
  
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
