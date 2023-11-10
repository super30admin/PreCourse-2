// Time Complexity :    O(logn)
// Space Complexity :   O(n)
//  Yes, It's run successfully
// No I don't face any problem.



class BinarySearch {
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int searchElement)
    {
        int a = arr.length;
        //Write your code here
        int mid = (l+r)/2;  // mid index

        if(r < l ){     //if right most pointer is less than left most pointer then return -1, termination condition of recursion
            return -1;
        }

        if(arr[mid] == searchElement){ // if search element present in the middle
            return mid;
        }
        else if ( arr[mid] < searchElement){ //  if search element is larger than mid element
            return binarySearch(arr, mid+1, r, searchElement);
        }
        else{ //  if search element is smaller than mid element
            return binarySearch(arr, l, mid-1, searchElement);
        }
    } 
  
    // Driver method to test above 
    public static void main(String args[]) 
    { 
        BinarySearch ob = new BinarySearch(); 
        int arr[] = { 2, 3, 4, 10, 40 }; 
        int n = arr.length; 
        int searchElement = 10;
        int result = ob.binarySearch(arr, 0, n - 1, searchElement);
        if (result == -1) 
            System.out.println("Element not present"); 
        else
            System.out.println("Element found at index " + result); 
    } 
} 
