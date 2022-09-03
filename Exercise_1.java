import javax.naming.spi.DirStateFactory.Result;

// Time Complexity :O(logn)
// Space Complexity :O(n)

// Any problem you faced while coding this : none


// Your code here along with comments explaining your approach
class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
        // find mid
        int mid = l+(r-l)/2;

        /*
         * if element is at mid return the index
         * if element is smaller than mid, find in left(decrement r to mid-1)
         * if element is greater than mid, find in right(increment l to mid+1)
         */

        if(l>r) {
            return -1;
        }
        if(x==arr[mid]){
            return mid;
        }
        
        else if(x<arr[mid]){
            r=mid-1;
        }else if (x>arr[mid]){
            l=mid+1;
        }
        // Call the function again with updated indices
        return binarySearch(arr, l, r, x);
        


    } 
  
    // Driver method to test above 
    public static void main(String args[]) 
    { 
        BinarySearch ob = new BinarySearch(); 
        int arr[] = { 2, 3, 4, 10, 40 }; 
        int n = arr.length; 
        int x = 4; 
        int result = ob.binarySearch(arr, 0, n - 1, x); 
        if (result == -1) 
            System.out.println("Element not present"); 
            else{
                System.out.println(result);
            }
    }
}
