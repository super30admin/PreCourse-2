import java.util.Arrays;


// Time Complexity : O(Nlog N base 2) (includes sorting time complexity aswell)
// Space Complexity : O(1) + O(N) -> O(N) (includes sorting space complexity aswell)

class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        // Since it has not been mentioned anywhere that array had been sorted, I sorted to make sure BS works fine.
        Arrays.sort(arr);
        while(l<=r){
            int mid = (l+r)/2;
            // If I find an element at mid'th index, I can return.
            if(arr[mid]==x){
                return mid;
            } else if (arr[mid]<x) {
                // If the value at the mid found less that the target element, we have to go right side. hence, l is placed after mid
                l=mid+1;
            } else {
                // If the value at the mid found greater than the target element, then, we have to go left side, hence, r is placed before mid
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
