
// time o(log(n)) and space o(1)
// divide the array in two halves, if mid number is smaller than target move end to left of mid else move start to right of mid
class BinarySearch {
    // Returns index of x if it is present in arr[l.. r], else return -1
    int binarySearch(int arr[], int start, int end, int x)
    {
        //Write your code here

        int mid = start + (end - start)/2;

        while(start <= end){
          mid = start + (end - start)/2;
          if(arr[mid] == x){
            return mid;
          }
          else if(arr[mid] < x){
             start = mid +1;
          }
          else{
            end = mid -1;
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
