class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
        int m;
        while(l <= r){
            m = (l+r)/2;
            // if the element is middle off array
            if(x==arr[m]){
                return m;
            }
            // if the middle of the element is gratear than x, searching right side
            else if (x<arr[m]){
                r = m-1;
            }
            // if the middle of the element is less than x, searching left side
            else{
                l=m+1;
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
