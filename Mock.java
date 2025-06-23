class Mock{

    public static int FindMissingInt(int nums[]){
        int low = 0;
        int high = nums.length -1;

        while(low <= high){
            int mid = low + (high-low)/2;
            if(mid==0)
                return nums[mid];

            if(nums[mid] - mid > 1){ //could be current element or on the left side , or maybe element the first element
                if(nums[mid-1]-(mid-1)==1 || mid==0)
                    return nums[mid]-1;
                else high = mid - 1;
            }

            else{       //missing element lies on the left
                low = mid + 1;
                }
                
        }
        
        return -1;
    }

    public static void main(String[] args){
        int nums[] = {1,3,4,5,6,7,8,9,10};
        int a = Mock.FindMissingInt(nums);
        System.out.println(a);
    }
}