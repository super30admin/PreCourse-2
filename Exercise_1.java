// Time Complexity : O(log n) as it traverses only half of the code
// Space Complexity : O(n) where n is len of array
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this :None
class BinarySearch {
    /*
    Binary search works only on sorted array.
    It looks if the ele is present before mid or after mid of ele.
    If then modified the value of l or r to search in half array.
    @params: array to search in, left index, right index, ele to be searched
    @return: Found value''s index / -1
     */
    int binarySearch(int arr[], int l, int r, int x) 
    {
        while(l<=r){
            int mid = (l+r)/2;
            if(x==arr[mid]){
                return mid;
            }
            if(x>arr[mid]){
                l=mid+1;
            } else{
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
            System.out.println("Element "+x+" not present");
        else
            System.out.println("Element "+x+" found at index " + result);
        x = 2;
        result = ob.binarySearch(arr, 0, n - 1, x);
        if (result == -1)
            System.out.println("Element "+x+" not present");
        else
            System.out.println("Element "+x+" found at index " + result);
        x = 5;
        result = ob.binarySearch(arr, 0, n - 1, x);
        if (result == -1)
            System.out.println("Element "+x+" not present");
        else
            System.out.println("Element "+x+" found at index " + result);
        int arr1[] = { 10, 30, 40, 50 };
        n = arr1.length;
        x = 30;
        result = ob.binarySearch(arr1, 0, n - 1, x);
        if (result == -1)
            System.out.println("Element "+x+" not present");
        else
            System.out.println("Element "+x+" found at index " + result);
        x = 50;
        result = ob.binarySearch(arr1, 0, n - 1, x);
        if (result == -1)
            System.out.println("Element "+x+" not present");
        else
            System.out.println("Element "+x+" found at index " + result);
        x = 100;
        result = ob.binarySearch(arr1, 0, n - 1, x);
        if (result == -1)
            System.out.println("Element "+x+" not present");
        else
            System.out.println("Element "+x+" found at index " + result);
    } 
} 
