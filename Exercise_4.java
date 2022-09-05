class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
void merge(int arr[], int l, int m, int r) 
    {  
        int[] temp=new int[r-l+1];
        int i=0,t=l,n=m;
       //Your code here  
        while(l<=n&&m+1<=r)
        {
            if(arr[l]<=arr[m+1])
            {
                temp[i]=arr[l];
                i++;
                l++;
            }
            else{
                temp[i]=arr[m+1];
                i++;
                m++;
            }


        }

        while(l<=n)
        {
            temp[i]=arr[l];
                i++;
                l++;
        }

        while(m+1<=r){
            temp[i]=arr[m+1];
                i++;
                m++;
            
        }

        for( i=0;i<temp.length;i++,t++)
        {
            arr[t]=temp[i];
        }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
    //Write your code here
        //Call mergeSort from here 
        if(l==r) return;
        int m=(l+r)/2;
        sort(arr, l, m);
        sort(arr, m+1, r);
        merge(arr,l,m,r);
    } 
  
    /* A utility function to print array of size n */
    static void printArray(int arr[]) 
    { 
        int n = arr.length; 
        for (int i=0; i<n; ++i) 
            System.out.print(arr[i] + " "); 
        System.out.println(); 
    } 
  
    // Driver method 
    public static void main(String args[]) 
    { 
        int arr[] = {12, 11, 13, 5, 6, 7}; 
  
        System.out.println("Given Array"); 
        printArray(arr); 
  
        MergeSort ob = new MergeSort(); 
        ob.sort(arr, 0, arr.length-1); 
  
        System.out.println("\nSorted array"); 
        printArray(arr); 
    } 
} 