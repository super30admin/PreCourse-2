/*
 * Time Complexity : O(nlogn) - since the runtime depends on half the input size( elements to be copared are decided based
 * on the current element is lesser or greater than the targer(x)).
 * 
 * Space Complexiy : Yet to determine
 * 
 *
 */
class Exercise_1 { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    {   
        //Assumption:  Array is always sorted(either ascending or descending)
        //Traverse the array of elments from the mid to either left or right based
        //which is determined by the value of the mid element either greater or lesser than the target/search value
        int m = 0;
        while(l <= r){
            m =  (l+r)/2;
            if(arr[m] == x){
                break;
            }
            if(arr[m] < x){
                l = m+1;
            }else{
                r = m-1;
            }
        }

     return m;
    } 
  
    // Driver method to test above 
    public static void main(String args[]) 
    { 
        Exercise_1 ob = new Exercise_1(); 
        int arr[] = { 2, 3, 4, 10, 40 }; 
        int n = arr.length; 
        int x = 2; 
        int result = ob.binarySearch(arr, 0, n - 1, x); 
        if (result == -1) 
            System.out.println("Element not present"); 
        else
            System.out.println("Element found at index " + result); 
    } 
} 
