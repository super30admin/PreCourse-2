class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        if(r>=l)
        {
            int m= l+(r-l)/2;
             if (arr[m] > x) //m is mid Element
             {
                  return binarySearch(arr, l, m - 1, x);
             }
             if (arr[m] == x)
             {
                 return m;
             }
            return binarySearch(arr, m + 1, r, x);
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


//time complexity : O(log n) binary search has this complexity
//space complexity : O(1)
//yes all test case passed and ran in leetcode
//recursive approach used
//no challenge faced as i did that question before.
