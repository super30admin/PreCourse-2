class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    
    public int search(int[] nums, int target) {
        return binarySearch(nums, 0, nums.length-1, target);        
    }
    public int binarySearch(int[] nums, int start, int end, int target){
        if(start> end) return -1;
        int mid= start + (end- start)/2;
        if(nums[mid]== target){
            return mid;
        }
        if(target> nums[mid]){
            start= mid+1;
            return binarySearch(nums, start, end, target);
        }
        else {
            end= mid-1;
            return binarySearch(nums, start, end, target);
        }
        //return -1;
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
