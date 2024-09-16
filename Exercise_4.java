class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
        int i=l;
        int j=m+1;
        int k=l;
        int b[] = new int[r+1];
        while(i<=m && j<=r){
            if(arr[i]<arr[j]){
                b[k]=arr[i];
                i++;
            }
            else{
                b[k]=arr[j];
                j++;
            }
            k++;
        }
        if(i>m){
            while(j<=r){
            b[k]=arr[j];
                j++;
                k++;
            }
        }
        if(j>r){
            while(i<=m){
                b[k]=arr[i];
                i++;
                k++;
            }
         }
        
        for(int t=l;t<=r;t++){
            arr[t]=b[t];
        }
 
        
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here 
        if(l<r){
            int mid=(l+r)/2;
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
        int arr[] = {12, 5,13 ,6, 7}; 
  
        System.out.println("Given Array"); 
        printArray(arr); 
  
        MergeSort ob = new MergeSort(); 
        ob.sort(arr, 0, arr.length-1); 
  
        System.out.println("\nSorted array"); 
        printArray(arr); 
    } 
} 