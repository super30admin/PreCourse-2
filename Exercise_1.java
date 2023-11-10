// Time Complexity : O(lon(n+1))
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : N/A
// Any problem you faced while coding this : Time Complexity. Unsure.


// Your code here along with comments explaining your approach

class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
        if(r>=l){
            int middle = l + (r-l)/2;
            if (arr[middle]==x){
                return middle;
            }
            else if(arr[middle]>x){
                return binarySearch(arr,l,middle-1,x);
            }
            else{
                return binarySearch(arr,middle+1,r,x);
            }
            }
        else{
            return -1;
        }
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
