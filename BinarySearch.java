//Time Complexity: O(log N)
//Auxiliary Space: O(1)

class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        while(l<=r){
            int mid = l + (r-l)/2;
            if (arr[mid]==x){
                System.out.println(arr[mid]);
                return mid;
            }
            if (arr[mid]<x){
                l=mid+1;
            }else{
                r=mid-1;
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
        for(int k = 0; k < arr.length; k++){
            System.out.println("array element " + arr[k] + " at index " + k);
        }
        int result = ob.binarySearch(arr, 0, n - 1, x); 
        if (result == -1) 
            System.out.println("Element not present"); 
        else
            System.out.println("Element found at index " + result); 
    } 
} 
