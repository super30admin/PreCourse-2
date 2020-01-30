/*
Binary Search works at O(log(n)), since everytime it checks the mid condition, the size of array is cut into half
*/


class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //while loop for the recursion
        while (l <= r) {
            //we find out the middle 
            int mid = (l + r) / 2 ; 
            //check if middle is the entity we are looking for (i.e. x)
            if (arr[mid] == x)
                return x ; 
            //conditions for recursion
            else if (arr[mid] > x) 
                r = mid - 1 ; 
            else
                l = mid + 1 ; 
        }
        //when item not found 
        return -1 ; 
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
