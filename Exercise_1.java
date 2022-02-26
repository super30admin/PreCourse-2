/*
Time Complexity: O(log(n))
Space Complexity: same as the question
Did this code successfully run on Leetcode : yes
Any problem you faced while coding this : no
*/

class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        while(l<=r){
            if(arr[(l+r)/2]==x) return x;
            if(x<arr[(l+r)/2]) r=((l+r)/2)-1;
            else if(x>arr[(l+r)/2]) l=((l+r)/2)+1;
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

