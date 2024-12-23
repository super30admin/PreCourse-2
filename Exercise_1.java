// Time Complexity : O(log n)
// Space Complexity :O(1) as we are not creating an extra array to store
// Did this code successfully run on Leetcode : I didn't find similar question on leetcode
// Any problem you faced while coding this : No




class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
        boolean isAsc = arr[l] < arr[r];    // It is checking if the array is sorted in ascending or Descending manner
        if(arr[l] < arr[r]){
            isAsc=true;
        }
        else{
            isAsc=false;
        }

        while(l<=r){                //Base condition if l > r then the element will not be present
            int mid=l+(r-l)/2;
            if(arr[mid]==x){        //If the mid is the target element then return it and no further execution
                return mid;
            }
            else{
                if(isAsc){            //If array is sorted in ascending order
                    if(x < arr[mid]){
                        r=mid-1;
                    }
                    else{
                        l=mid+1;
                    }
                }
                else{               //If array is sorted in descending order
                    if(x < arr[mid]){
                        l=mid+1;
                    }
                    else{
                        r=mid-1;
                    }
                }
            }
        }
        return -1;                  //If the target element is not present
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
