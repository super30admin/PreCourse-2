class BinarySearch { 
    // Time Complexity : O(log n)
    // Space Complexity :O(1) since i'm using a constant variable to store the middle
    // Did this code successfully run on Leetcode :
    // Any problem you faced while coding this :
    /*  intially coudlnt figure out how can I point ot the correct index l + (r-l) / 2;
        so after  long thime I realized I can either add l (or) r to the middleIndex 
        to point to the middleIndex relative to that section
        */
    
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //base condition 
        if(r < l ) return -1;
        
        int middleIndex = l + (r-l) / 2;
        middleIndex = l + middleIndex ;
        if(arr[middleIndex] == x) return middleIndex;
        if(arr[middleIndex] < x ) return binarySearch(arr, middleIndex+1, r, x);
        else  return binarySearch(arr, l, middleIndex-1, x);

    } 
  
    // Driver method to test above 
    public static void main(String args[]) 
    { 
        BinarySearch ob = new BinarySearch(); 
        int arr[] = { 2, 3, 4, 10, 40 }; 
        int n = arr.length; 
        int x = 1; 
        int result = ob.binarySearch(arr, 0, n - 1, x); 
        if (result == -1) 
            System.out.println("Element not present"); 
        else
            System.out.println("Element found at index " + result); 
    } 
} 
