/*
    Time Complexity : O(Log n)
*/

public class Exercise_1 { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
        int mid_index = l + (r-l) /2;
        if(r>=l){
            if(arr[mid_index] == x) return mid_index;
            if(x > arr[mid_index]) return binarySearch(arr, mid_index+1, r, x);
            if(x< arr[mid_index]) return binarySearch(arr, l, mid_index-1, x);
        }
        return  -1;
         
    }
    
    int binarySearch_iterative(int arr[], int x) 
    { 
        int l = 0;
        int r = arr.length - 1;
        while (l<=r){
            int mid_index = l + (r-l)/2;
            if (arr[mid_index] == x) return mid_index;
            if (x > arr[mid_index]) l = mid_index + 1;
            else if (x < arr[mid_index]) r = mid_index -1;
        }
        return -1;
    }
  
    // Driver method to test above 
    public static void main(String args[]) 
    { 
        Exercise_1 ob = new Exercise_1(); 
        int arr[] = { 2, 3, 4, 10, 40 }; 
        int n = arr.length; 
        int x = 10; 
        int result = ob.binarySearch(arr, 0, n - 1, x); 
        if (result == -1) 
            System.out.println("Element not present"); 
        else
            System.out.println("Element found at index " + result); 
    
        int result1= ob.binarySearch_iterative(arr, x); 
        if (result1 == -1) 
            System.out.println("Element not present"); 
        else
            System.out.println("Element found at index in iterative approach " + result1); 
    } 
} 
