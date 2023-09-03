class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here

        if (l<=r){

        int mid =(l+r)/2;

        if (x==arr[mid]){
            return mid;
        }

        if (x<arr[mid]){
            return binarySearch(arr, 0, mid-1, x);
        }
        else {
            return binarySearch(arr, mid+1, r, x);

        }
    }
        return -1;
    } 
  
    // Driver method to test above 
    public static void main(String args[]) 
    { 
        BinarySearch ob = new BinarySearch(); 
        int arr[] = { 2, 3, 4, 10, 40, 56, 67, 78, 89 }; 
        int n = arr.length; 
        int x = 67; 
        int result = ob.binarySearch(arr, 0, n - 1, x); 
        if (result == -1) 
            System.out.println("Element not present"); 
        else
            System.out.println("Element found at index " + result); 
    } 
} 
