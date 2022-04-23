//Time Complexity : O(logN)
//Space Complexity : O(1)
class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
        //Run the while loop until l is less than or equal to right
        while(l<=r){
            //take a new variable mid which points at middle element index of the arr[]
            int mid = (l+r)/2;
            //If x is less than middle element of arr (arr[mid]) then search for element from l=0 to r=middle-1 index
            if(x<arr[mid]){
                r=mid-1;
                mid=(l+r)/2;
            }
            //else if x is greater than middle element of arr (arr[mid]) then search for element from l=middle+1 to r index
            else if(x>arr[mid]){
                l=mid+1;
                mid=(l+r)/2;
            }
            //else if arr[mid] itself is x return mid
            else{
                return mid;
            }
        }
    //if element is not found return -1
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
