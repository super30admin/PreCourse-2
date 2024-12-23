class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    
    // Time Complexity: O(log(n))
    // Space Complexity: O(1)
     // since we are reducing our searching space by half in each step, it will decrease at a log(n) pace
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
        while (l <= r){
            int pos = (l+r)/2; 
        if (x > arr[pos]){
            l = pos +1;
        } else if (x < arr[pos]){
            r = pos -1;
        }
        else if (x == arr[pos]){
            return pos;
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
