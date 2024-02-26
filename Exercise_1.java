/*Time Complexity:
 * Best case : O(1);
 * Worst case : O(log n); where n is number of elements in the array
 * 
 * Space Complexity:O(log n); where n is number of elements in the array, since we are using reccursive approch
 * 
 * Output : Element found at index 3
 */

class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
        if (r >= 1){ // Finding mid index
            int mid = (l + (r-1))/2;

            if (arr[mid]==x){ 
                return mid;
            }
            if (arr[mid] < x){ //we can ignore the left half
                return binarySearch(arr, mid+1, r, x);
            }else{
                return binarySearch(arr, l, mid-1, x); // we can ignore right half
            }
        }
        return -1; //If X is not present in the array
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
