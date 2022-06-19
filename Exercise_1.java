// Time Complexity : o(log(n)) since we'll elimate half of the elements from the array in each iteration 
// Space Complexity : o(n) to store the n elements in an array
// Did this code successfully run on Leetcode : yes
// Any problem you faced while coding this : no
// check if the middle index element is equal to x. if not, check if x is greater than middle element so its on the right sub array so change l to middle+1 otherwise its in the left sub array to change r to middle -1.
class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
        while(l<=r){
            int middle = l + ((r-l)/2);
            if(arr[middle] == x)
                return middle;
            else if(arr[middle] < x)
                l= middle + 1;
            else 
                r = middle -1;
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
