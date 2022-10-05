//Time complexity : O(logN)
//Space Complexity: O(N)

class BinarySearch {
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x)
    {
        //Write your code here


        while(l<=r)
        {

            if(arr[(l+r)/2] == x){
                return (l+r)/2;
            }
            else if(arr[(l+r)/2] > x)   {
                r= (l+r)/2 -1;

            }else if(arr[(l+r)/2] < x){
                l=(l+r)/2 +1;
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