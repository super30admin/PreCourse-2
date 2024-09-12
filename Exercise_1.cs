using System;
class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int[] arr, int l, int r, int x) 
    { 
        //Write your code here
        if(r>=l){
            int mid=l+(r-1)/2;
            //if element is in mid position
            if(arr[mid] == x)
            return mid;
            //if element is in left portion
            return binarySearch(arr, l , mid-1, x);
            //if element is in rght portion 
            return binarySearch(arr, mid+1 , r, x);
        }
        return -1;//if element is not present
    } 
  
    // Driver method to test above 
    public static void main(String[] args) 
    { 
        BinarySearch ob = new BinarySearch(); 
        int[] arr = { 2, 3, 4, 10, 40 }; 
        int n = arr.length; 
        int x = 10; 
        int result = ob.binarySearch(arr, 0, n - 1, x); 
        if (result == -1) 
            Console.WriteLine("Element not present"); 
        else
            Console.WriteLine("Element found at index " + result); 
    } 
} 
