 class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) {
            int y= (int) Math.floor((r-l)/2)+ l;
            if(x<arr[y]){
                return binarySearch(arr, l,  y-1,  x);
            }
            else if(x>arr[y]){
                return binarySearch(arr, y+1,  r,  x);
            }
            else if(x==arr[y]){
                return y;
                
            }
            else{
                return -1;
               
            }
       
    }   
            
            
           
        
    
   
    
  

    public static void main(String args[]) 
    { BinarySearch ob = new BinarySearch(); 
        int arr[] = { 2, 3, 4, 10, 40 }; 
        int n = arr.length; 
        int x = 10; 
        int result = ob.binarySearch(arr, 0, n - 1, x); 
        if (result == -1) {
            System.out.println("Element not present"); 
        }
        else{
            System.out.println("Element found at index " + result); 
        }
    } 
}
