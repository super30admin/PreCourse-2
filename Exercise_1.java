// Time complexity and Space complexity is O(Logn)
class BinarySearch {
    // Returns index of x if it is present in arr[l.. r], else return -1
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
        if(r>=l){
            int mid = l + (r-l)/2;

            if(arr[mid] == x) //if element is at the middle
                return mid;

            if(arr[mid] > x) // if element is less than mid element
                return binarySearch(arr, l, mid-1, x);

            return binarySearch(arr, mid+1, r, x); // if element is greater than mid element
        }
        return 0;
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
