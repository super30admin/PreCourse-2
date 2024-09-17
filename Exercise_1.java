public class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
        //Doing iterative binary search
        // Time complexity O(logn)  Space Complexity O(1)
         l = 0;
         r = arr.length - 1;
        while(l<=r)
        {
            //calculate the mid of the array
            int mid = l+ (r-l)/2;
            // if middle element is the required element, return the index
            if(arr[mid] == x)
            {
                return mid;
            }
            // if element is greater than mid element then increment
            if(arr[mid] < x)
            {
                l = mid+1;
            }
            
            else
            {
                r = mid-1;
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
