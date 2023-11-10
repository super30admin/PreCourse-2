class Exercise_1{ 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    {   
        //check whether the left is less than right means that the element lies between the two
        if(r>=l){
            //calculate mid element
            int mid=l+(r-l)/2;
            //if the mid element is equal to the key return it
            if(arr[mid]==x){
                return mid;
            } 
            //if the mid element is greater than key , search recursilvely in the first half of array
            if(arr[mid]>x){
                return binarySearch(arr,l,mid-1,x);
            }
             //if the mid element is smaller than key , search recursilvely in the second half of array
            else{
                return binarySearch(arr,mid+1,r,x);
            }
        }
        //if the key is not found return -1
        return -1;
        
    } 
  
    // Driver method to test above 
    public static void main(String args[]) 
    { 
        Exercise_1 ob = new Exercise_1(); 
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
