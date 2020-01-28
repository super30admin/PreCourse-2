class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int left, int right, int target) 
    { 
        //Calculate mid value
       int mid = (left+right)/2;

       //Left > right => value not found
       if(left > right) 
            return -1;

        // If target < mid value, change right to mid-1
        if(target < arr[mid]) {
            return binarySearch(arr,left,mid-1,target);
        }
        // Target > mid, change left to mid+1
        else if(target > arr[mid]) {
            return binarySearch(arr,mid+1,right,target);
        }
        else 
            return mid;
    } 
  
    // Driver method to test above 
    public static void main(String args[]) 
    { 
        BinarySearch ob = new BinarySearch(); 
        int arr[] = { 2, 3, 4, 10, 40, 400, 500, 920, 5403, 23054, 45687, 90125 }; 
        int n = arr.length; 
        int x = 999; 
        int result = ob.binarySearch(arr, 0, n - 1, x); 
        if (result == -1) 
            System.out.println("Element not present"); 
        else
            System.out.println("Element found at index " + result); 
    } 
} 
