class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { int mid;
        //Write your code here
        if(r>l) {

            if (arr[0] < arr[1]) {
                System.out.println("Provided numbers in Ascending order");
                while(l<=r){

                     mid=getMidIndex(l,r);
                    if(arr[mid]>x){
                        r=mid-1;
                    }else if(arr[mid]<x){
                        l=mid+1;
                    }else if(arr[mid]==x){
                        return mid;
                    }
                }
                System.out.println("Element unAvailable in the list");
                return -1;
            }
            else{
                System.out.println("provided numbers are in descending order");
                while(l<=r){

                    mid=(l+r)/2;
                    if(arr[mid]<x){
                        r=mid-1;

                    }else if(arr[mid]>x){
                        l=mid+1;
                    }else if(arr[mid]==x){
                        return mid;
                    }
                }

                return -1;
            }
        }
        else{
            System.out.println("Provided l<r , please change the index and run again");
            return -1;
        }
    } 

    int getMidIndex(int low,int high){
        return (low+high)/2;
    }
    // Driver method to test above 
    public static void main(String args[]) 
    { 
        BinarySearch ob = new BinarySearch(); 
        int arr[] = { 2, 3, 4, 10, 40 }; 
        int n = arr.length; 
        int x =40 ;
        int result = ob.binarySearch(arr, 0, n - 1, x); 
        if (result == -1) 
            System.out.println("Element not present"); 
        else
            System.out.println("Element found at index in case1 " + result);

    BinarySearch ob2=new BinarySearch();
     arr=new int[]{100,99,98,4,2,1,0};
     n=arr.length;
     x=0;
     result=ob2.binarySearch(arr,0,n-1,x);
     if(result==-1){
         System.out.println("Element not present");
     }else{
         System.out.println("element found at index in case2 "+ result);
     }

    }
} 
