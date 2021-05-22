// TC : O(log n). This is because after k iterations the size of the array is n/2^k and hence the array becomes half at every iteration
//SC : For iterative approach : O(1) and for recursive approach O(lon N) due to recursive call stack.
class BinarySearch {
    // Returns index of x if it is present in arr[l.. r], else return -1

    //recursive approach for BinarySearch
    int binarySearch(int[] arr, int left, int right, int x)
    {
        //Write your code here
        if(right>=left)
        {
            //mid = (left+right)/2 but we use this expression to avoid integer overflow
            int mid = (right-left)/2 + left;

            //target element is smaller than the middle element that means, the target element lies in the left half
            if(x<arr[mid])
                return binarySearch(arr,left, mid-1,x);

                //target element is greater than the middle element that means it lies in the second half of the array
            else if(x>arr[mid])
                return binarySearch(arr,mid+1, right,x);
            else
                return mid;
        }

        //if the target element does not belong to the array then return -1
        return -1;

    }


    //iterative approach to binarySearch
    int binarySearch(int[] arr,int x)
    {
        int left=0, right = arr.length-1;

        while (left<=right)
        {
            //mid = (left+right)/2 but we use this expression to avoid integer overflow
            int mid = (right-left)/2 + left;

            //target element is smaller than the middle element that means, the target element lies in the left half
            if(x < arr[mid])
                right = mid -1;

                //target element is greater than the middle element that means it lies in the second half of the array
            else if(x >arr[mid])
                left = mid +1;
            else
                return mid;

        }

        //if the target element does not belong to the array then return -1
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

        x = 3;
        result = ob.binarySearch(arr, x);
        if (result == -1)
            System.out.println("Element not present");
        else
            System.out.println("Element found at index " + result);
    }
}