// Time Complexity :0(log n)
// Space Complexity :0(1)
// Did this code successfully run on Leetcode : yes

class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
          int low=0;
    int high= arr.length-1;
    int mid= low+(high-low)//2;

    while(low<high){
        if(arr[mid] == x)
        return mid;
    }
    else if(arr[mid] < x){
        low=mid+1;
    } else high=mid-1;
} return -1;
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
