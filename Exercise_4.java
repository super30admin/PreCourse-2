class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
       int [] temp=new int[r-l+1];
       int tempidx=0;
       int lidx=l;
       int ridx=m+1;
       while(lidx<=m&&ridx<=r){
        if(arr[lidx]<=arr[ridx]){
            temp[tempidx++]=arr[lidx++];
        }
        else{
            temp[tempidx++]=arr[ridx++];
            
        }
       }
       while (lidx<=m) {
        temp[tempidx++]=arr[lidx++];
        
       }
       while (ridx<=r) {
        temp[tempidx++]=arr[ridx++];
        
       }
       for(int i=0,k=l;i<temp.length;i++,k++){
        arr[k]=temp[i];
       }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
        if(l>=r)return;
        int mid=l+(r-l)/2;
        sort(arr,l,mid);
        sort(arr,mid+1,r);
        merge(arr,l,mid,r);
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