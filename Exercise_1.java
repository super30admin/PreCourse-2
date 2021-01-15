import java.util.*;

class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
        if(arr.length < 1 || r < l){
            return -1;
        }

        if(arr[0]==x){
            return 0;
        }
        
        Arrays.sort(arr);
        
        int mid =  (l+r)/2;

        //System.out.println(mid);
        if(x == arr[mid]){
             return mid;
        }
         if(x < arr[mid]){
            return binarySearch(arr,l,mid-1,x);
        }
         if(x > arr[mid]){
            return binarySearch(arr,mid+1,r,x);
        }
        return -1;
        
        
    } 
   
    // Driver method to test above 
    public static void main(String args[]) 
    { 
        BinarySearch ob = new BinarySearch(); 
        int arr[] = {  2, 3, 4, 10, 40 }; 
        int n = arr.length; 
        int x = 2; 
        int result = ob.binarySearch(arr, 0, n - 1, x); 
        // int arr2[] = { 2 }; 
        // result = ob.binarySearch(arr2, 0, 0, x); 

        // int arr3[] = { };
        // result = ob.binarySearch(arr3, 0, -1, x); 
        if (result == -1) 
            System.out.println("Element not present"); 
        else
            System.out.println("Element found at index " + result); 
    } 
} 


