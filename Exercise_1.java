// Time Complexity: O(logN)
// Space Complexity: O(1)
// Any problem you faced while coding this : No
class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
        while(l<=r){
            // we get the mid element, and we check if our mid element is the same as the given element.
            int mid=l+(r-1)/2;
            if(arr[mid]==10)
            {
                return mid;
            }
            // if mid>x, element is in the first half of the array, make the right pointer before middle
            else if(arr[mid]>x)
            {
                r=mid-1;
            }
            // element is in the 2nd half, move the left pointer after the middle element
            else
            {
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
        int x = 10; 
        int result = ob.binarySearch(arr, 0, n - 1, x); 
        if (result == -1) 
            System.out.println("Element not present"); 
        else
            System.out.println("Element found at index " + result); 
    } 
} 
