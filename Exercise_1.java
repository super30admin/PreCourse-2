public class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int low, int high, int x) 
    { 
        //Write your code here
        int mid=low+(high-low)/2;
        while(low<high){
            mid=low+(high-low)/2;
            if(arr[mid]==x)
                return mid;
            else if(x<arr[mid]){
                high=mid-1;
            }else{
                low=mid+1;
            }
        }
        return arr[low]==x ? low : -1;
    } 
  
    // Driver method to test above 
    public static void main(String args[]) 
    { 
        BinarySearch ob = new BinarySearch(); 
        int arr[] = { 2, 3, 4, 10, 40 }; 
        int n = arr.length; 
        int x = 14; 
        int result = ob.binarySearch(arr, 0, n - 1, x); 
        if (result == -1) 
            System.out.println("Element not present"); 
        else
            System.out.println("Element found at index " + result); 
    } 
} 