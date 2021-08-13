class BinarySearch { 
   // Time Complexity : O(N)
    // Space Complexity : O(1)
    // Did this code successfully run on Leetcode : Yes
    // Any problem you faced while coding this : No
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //using loop to search required number
        
        for(int i =0;i< arr.length;i++){
           if(arr[i]==x){
               //returns the required index
               return i;
           }
        }
        // return -1 if the number is not found
        return -1;
    } 
  
    // Driver method to test above 
    public static void main(String args[]) 
    { 
        BinarySearch ob = new BinarySearch(); 
        int arr[] = { 2, 3, 4, 10, 40 }; 
        int n = arr.length; 
        int x = 3; 
        int result = ob.binarySearch(arr, 0, n - 1, x); 
        if (result == -1) 
            System.out.println("Element not present"); 
        else
            System.out.println("Element found at index " + result); 
    } 
} 
