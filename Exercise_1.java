//Time complexity O(logn)
//Space complexity O(1)

class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        int pivot  = (l+r)/2;
        if(arr[pivot]==x){
            return pivot;
        }else if(arr[pivot]>x){
            r=pivot;
             return binarySearch(arr,l,r,x);
        }else{
            l = pivot;
            return binarySearch(arr,l,r,x);
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
