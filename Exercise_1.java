//time complexity is O(log n)
//space complexity is O(1)
class BinarySearch {
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    {
        //if right is greater or equal to left
        if( r >= l) {
            //take mid element , to avoid int overflow subtract r-l to get r
            int mid = l + (r-l) /2;

            // if  middle element is the target, return middle element
            if(arr[mid] == x)
                return mid;
            // if middle element is greater than target,move right to mid -1,call recursively again
            else if( arr[mid] > x) {
              return  binarySearch(arr, l, mid-1, x);
            }
            else
                // if middle element is less  than target,move left  to mid +1,call recursively again
               return  binarySearch(arr, mid +1, r, x);

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
