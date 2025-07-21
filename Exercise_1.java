//Time Complexity: O(nlogn) 
//Space Complexity: O(1)
//Did the code successfully run on Leetcode: Yes
//Any problem faced while coding this: No

class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
        int left=0;
        int right = arr.length-1;
        
        while(left<=right){
            int mid= (left+right)/2;
            if (arr[mid]==x){
                return mid;
            }
            if(arr[mid]<x){
                left=mid+1;
               
            }else{
                 right=mid-1;
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
