//Time Complexity : O(log2n)
//Space Complexity : Olog(n)
class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
        //Recursive implementation 
        //checking the Array 
        //right element=high,
        //left element= low 
        //so right >= left
        if(r>=l){
            //Calculating the middle value of array
            int mid = l+(r-l)/2;
            if(x == arr[mid])
            return mid;

            if (arr[mid]>x)//If middle value is greater than X, otherwise check for middle value lessthan x
                return binarySearch(arr,l,mid-1,x);       

            return binarySearch(arr,mid+1,r,x);
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
