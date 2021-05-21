class MergeSort 
{ 
    int ln,rn,i,j,k;
    int l1[]=new int[ln];
    int r1[]=new int[rn];
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       ln=m-l+1;
       rn=r-m;
       int l1[]=new int[ln];
       int r1[]=new int[rn];
       i=0;j=0;k=l;
       
       for(int a=0;a<ln;a++)
       {
           l1[a]=arr[a+l];
       }
       for(int b=0;b<rn;b++)
       {
           r1[b]=arr[b+m+1];
       }
       while(i<ln && j<rn)
       {
           if(l1[i]<r1[j])
           {
               arr[k]=l1[i];
               i++;
               
           }
           else
           {
               arr[k]=r1[j];
               j++;
               
           }
           k++;
       }
       while (i<ln)
       {
            arr[k]=l1[i];
            i++;
            k++;
       }
       while(j<rn)
       {
            arr[k]=r1[j];
            j++;
            k++;
       }
       //Your code here  
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    {
        if(l<r)
        {
            int m =(l+r)/2;
            
            sort(arr, l, m);
            sort(arr, m + 1, r);
 
            merge(arr, l, m, r);
        } 
	//Write your code here
        //Call mergeSort from here 
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