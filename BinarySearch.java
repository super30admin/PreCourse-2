class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int low, int high, int target) 
    { 
        //Write your code here
        while(high >= low){
            int mid = (high+low)/2;

            if(target == arr[mid]){
                return mid;
            }else if(target >= arr[mid]){
                low = mid+1;
            }else{
                high = mid-1;
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
//TC - O(log n)
//SC - O(1)