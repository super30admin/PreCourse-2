//Time Complexity : O(log n)
//Space Complexity : O(1) 
//Did this code successfully run on Leetcode : Yes 


class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        l=0;
        r= arr.length-1;
  
        while(l<=r){
  
         int m= (l+r)/2;
         if(x<arr[m])
          r= m-1;
         else if(x>arr[m])
          l= m+1;
         else{
          return m;
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
