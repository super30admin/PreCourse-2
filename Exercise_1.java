public class BinarySearch {
    /*
    Time Complexity : O(log N)
    Space Complexity : O(1)
     */
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    {
        int result=-1;
        while(l<=r) {
            if(arr[l] == x){
                result = l;
                break;
            } else if(arr[r] == x) {
                result = r;
                break;
            }
            l++;
            r--;
        }
        return result;
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
