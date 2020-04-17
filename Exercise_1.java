//Time Complexity:O(logn)
//Space:O(1)	

class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1
    int fin=-1;
    int binarySearch(int arr[], int l, int r, int x) 
    {
        int mid=(l+r)/2;

        if(arr[mid]==x) {
            
            fin=mid;
            return mid;
        }
         if(mid<0||mid>arr.length) {

             return -1;
         }
        if(x<arr[mid])
        {
            binarySearch(arr,l,mid-1,x);
        }
        if(x>arr[mid])
            binarySearch(arr,mid+1,r,x);


       return fin;//Was confuesd how to frame the return statement thus created global variable, looking to have a better solution than this.
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
