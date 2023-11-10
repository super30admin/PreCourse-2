class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        int mid = (l + r)/2;
        int res=0;
        while(l <=r){
            if(arr[mid]<x){
                l = mid+1;
            }
            else if(arr[mid]==x){
                res = mid;
                break;
            }
            else{
                r = mid-1;
            }
            mid = (l+r)/2;
        }
        if(l>r){
            res = -1;
        }
        return res;

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
