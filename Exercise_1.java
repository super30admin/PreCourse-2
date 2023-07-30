// Time Complexity : O(log n)
// Space Complexity : O(log n) because of recurssion
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : NO
class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
       
        //Write your code here
        if(l<=r){   //  Check if left index is less than or equal to right index
        int mid=(l+r)/2;  //Caluculate mid value
        // if the target value is equal to value present in array at index mid return mid;
        if(arr[mid]==x)    
         return mid;   
        // If target value x is greater than value present in array at index mid,
        //all the elements left to mid is less than target and doesn't need to be checked    
        else if(x>arr[mid]){
            l=mid+1;   
            // Search from mid+1 index
            return binarySearch(arr,l,r,x);
        }
        // If target value x is less than value present in array at index mid,
        //all the elements right to mid is greater than target and doesn't need to be checked    
        else {
            r=mid-1;
             //search from mid-1 index
            return binarySearch(arr,l,r,x);
        }
    }
        return -1;  // If element not found return -1.
        
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
