class BinarySearch {
    public static void main(String args[])
    {
        BinarySearch ob = new BinarySearch();
        int arr[] = { 2, 3, 4, 10, 40 };
        int n = arr.length;
        int x = 10;
        int result = binarySearch(arr, 0, n - 1, x);
        if (result == -1)
            System.out.println("Element not present");
        else
            System.out.println("Element found at index " + result);
    }

    public static int binarySearch(int[] nums,int l, int u, int target){
        if(u>=l){
            int mid=l+((u-l)/2);
            if(nums[mid]==target){
                return mid;
            }
            if(nums[mid]>target){
                return binarySearch(nums,l,mid-1,target);
            }
            if(nums[mid]<target){
                return binarySearch(nums,mid+1,u,target);
            }
        }
        return -1;
    }
}
