class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
        if(r>=l){
            int mid = l+(r-l)/2;
            System.out.println("Mid idx: "+mid+" arr["+mid+"] is: "+arr[mid]);
            //Need to check recursively for element
            if(x==arr[mid]) {
                System.out.println("Element found at index: "+mid+" arr["+mid+"] is: "+arr[mid]);
                return mid;   
            }
            else if(x<arr[mid]) {
                // r=mid-1;
                System.out.println("Checking left b/w indexes "+l +" & "+(mid-1));
                return binarySearch(arr, l,mid-1, x);
            }
            else if(x>arr[mid]) {
                // r=mid+1;
                System.out.println("Checking right b/w indexes "+(mid+1) +" & "+r);
                return binarySearch(arr,mid+1,r,x);
            }
        }
        
        return -1;
    } 
  
    // Driver method to test above 
    public static void main(String args[]) 
    { 
        BinarySearch ob = new BinarySearch(); 
        int arr[] = { 2, 3, 4,10, 40, 50}; 
        int n = arr.length; 
        int x = 10; 
        int result = ob.binarySearch(arr, 0, n - 1, x); 
        if (result == -1) 
            System.out.println("Element not present"); 
        else
            System.out.println("Element found at index " + result); 
    } 
} 
