//Time complexity O(log n)
//Space Complexity O(1)

class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    //This is a recursive approach, we check the target element with the middle element of the array passed, let us call indices of start and end elements as l, r
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
       if ( l <= r){
            int mid = l + (r - 1) / 2;
        // if target element == mid element of the array passed
        if (arr[mid] == x) return mid;
        
        // if mid element < target element of the array passed
        else if(arr[mid] < x){
            // Search for element in the greater half of the array
           return binarySearch(arr, mid + 1 , r, x);
        }
           
        // if target  mid element > target element of the array passed
        else if (arr[mid] > x) {
            // Search for element in the lower half of the array
            return binarySearch(arr, l , mid - 1  , x);
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
        //Sorting Array, Binary Search only works when elements are sorted. 
        Arrays.sort(arr);
        
        int result = ob.binarySearch(arr, 0, n - 1, x); 
        if (result == -1) 
            System.out.println("Element not present"); 
        else
            System.out.println("Element found at index " + result); 
    } 
} 
