//Overall Time Complexity is O(logn).
//Overall Space Complexity is O(logn).
class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        while(l<=r){

            int mid = l+(r-l)/2; // Find the mid 
            if(arr[mid] == x){ // Check if mid is the element that we are searching 
                return mid; // If yes return mid.
            }
            else{
                if(x<arr[mid]){ // Check if target is less than the mid element 
                    r = mid -1; // Then move the right pointer to mid-1 position
                }
                else{
                    l = mid+1;// Else move the left pointer to mid+1 position
                }
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
