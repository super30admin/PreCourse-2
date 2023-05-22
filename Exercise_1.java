// Time Complexity :
    //best case: O(1), if the element is found at the middle of the list
    //worst case and avg case: O(log(n)), since we would be dividing the list in half in each iteration
// Space Complexity : O(n) where n is number of elements and we will need an array of length n
// Did this code successfully run on Leetcode :N/A
// Any problem you faced while coding this :
//Assumptions: assumed that the input array is always sorted
class BinarySearch {
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    {
        int index = -1;
        int mid = -1;

        //input validations
        if(arr.length == 0 || l < 0 || r <0)
        {
            return index;
        }

        while(r >= l)
        {
            mid = (l+r)/2; //this should return the floor of the avg in case there are even no. of elements
            if(arr[mid] == x)
            {
                return mid;
            }
            else if(x > arr[mid])
            {
                //search the right/higher half of the list
                l = mid +1;
            }
            else
            {
                //search the left/lower half of the list
                r = mid -1;
            }
        }
        return index;
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
