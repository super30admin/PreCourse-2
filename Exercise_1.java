// Time Complexity : O(logN), where N is length of an array. So O(log5 base 2)
// Space Complexity : O(1)

class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        while(l <= r){
            int mid = l + (r - l)/2;
            if(x > arr[mid]){
                l = mid + 1;
            } else if(x < arr[mid]){
                r = mid - 1;
            } else return mid;
        }
        return -1;
    } 
  
    // Driver method to test above 
    public static void main(String args[]) 
    { 
        BinarySearch ob = new BinarySearch(); 
        int arr[] = { 2, 3, 4, 10, 40 }; 
        int n = arr.length; 
        int x = 3; 
        int result = ob.binarySearch(arr, 0, n - 1, x); 
        if (result == -1) 
            System.out.println("Element not present"); 
        else
            System.out.println("Element found at index " + result); 
    } 
} 
