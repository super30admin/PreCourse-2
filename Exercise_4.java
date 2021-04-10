class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r]
    static int tempArr[];
    void merge(int arr[], int l, int m, int r) 
    {  
        //System.out.println("Inside Merge l= "+l+" r= "+r+" m= "+m);
        
       //Your code here
       int lptr = l, rptr = m+1, index = l;
       if(lptr>rptr){
        return;
       }

       else if(lptr==rptr){
           tempArr[lptr] = arr[lptr];
       }

       else{
            while(lptr<=m && rptr<=r)
            {
                if(arr[lptr]<=arr[rptr])
                {
                    tempArr[index] = arr[lptr];
                    lptr++;
                    index++;
                }
                else
                {
                    tempArr[index] = arr[rptr];
                    rptr++;
                    index++;
                }
            }
            while(lptr<=m)
            {
                tempArr[index] = arr[lptr];
                index++;
                lptr++;
            }
            while(rptr<=r)
            {
                tempArr[index] = arr[rptr];
                index++;
                rptr++;
            }
            for(int i=l;i<=r;i++)
            {
                arr[i] = tempArr[i];
            }
        }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here
        //System.out.println("Inside sort l "+l+"r "+r);
       if(l<r){
        int mid = l + (r-l)/2;
        sort(arr,l,mid);
        sort(arr,mid+1,r);
        merge(arr,l,mid,r);
       }
        
       
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
        
        tempArr = new int[arr.length];
        // for(int i=0;i<arr.length;i++){
        //     tempArr[i] = arr[i];
        // }
  
        System.out.println("Given Array"); 
        printArray(arr); 
  
        MergeSort ob = new MergeSort(); 
        ob.sort(arr, 0, arr.length-1); 
  
        System.out.println("\nSorted array"); 
        printArray(arr); 
    } 
} 