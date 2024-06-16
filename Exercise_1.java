// Time Complexity :O(logn)-> Since the loop divides itself into half each time it traverses through the array based on the mid and the value in search.
// Space Complexity :O(1) we are using only one variable alled mid.
// Did this code successfully run on Leetcode :Yes
// Any problem you faced while coding this : No


// Your code here along with comments explaining your approach

// Iterate through the array and have two variable insisting a left pointer and a right pointer. When the mid point of array matches the searching element then return the respective index else keep searching inside the loop until the value of mid is less than or greater than x.


class Exercise_1 { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
        int mid=0;
        while(l<=r){
            mid=(l+r)/2;
            if(arr[mid]==x)
                return mid;
            else if(arr[mid]>x)
                r=mid-1;
            else if(arr[mid]<x)
                l=mid+1;            
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
    } 
} 
