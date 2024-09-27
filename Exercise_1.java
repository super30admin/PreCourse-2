//Time complexity: O(log n)
//Space complexity: O(1)
class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    //iterative
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        while(l <= r){
            int midpoint = l + (r - l)/2;
            if(x == arr[midpoint]){
                return midpoint;
            }
            else if(x < arr[midpoint]){
                r = midpoint - 1;
            }
            else {
                l = midpoint + 1;
            }
        }
        return -1;
    } 
    
    int binarySearchR(int arr[], int l, int r, int x){
        //base
        if(r < l) return -1;
        
        //logic
        int midpoint = l + (r - l)/2;
        if(x == arr[midpoint]){
            return midpoint;
        }
        else if(x < arr[midpoint]){
            return binarySearchR(arr, l, midpoint - 1, x);
        }
        else {
            return binarySearchR(arr, midpoint + 1, r, x);
        }
    }
  
    // Driver method to test above 
    public static void main(String args[]) 
    { 
        BinarySearch ob = new BinarySearch(); 
        int arr[] = { 2, 3, 4, 10, 40 }; 
        int n = arr.length; 
        int x = 2; 
        int result = ob.binarySearch(arr, 0, n - 1, x); 
        if (result == -1) 
            System.out.println("Element not present"); 
        else
            System.out.println("Element found at index " + result); 
    } 
} 
