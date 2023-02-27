public class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
        
        if(arr[r]==x)
        {
            return r;
        }
        else
        {
            boolean flag=false;
            int m=(l+r)/2;
            while(arr[m]!=x && l!=r)
            {
                System.out.println(l);
                System.out.println(r);
                if(arr[m]<x)
                {
                    l = m;
                    m = (l+r)/2;
                }
                else if(arr[m]>x)
                {
                    r = m;
                    m = (l+r)/2;
                }
                if(arr[m]==x)
                {
                    flag = true;
                }
            }
        
            if(flag)
                return m;
            else
                return -1;
        }
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
