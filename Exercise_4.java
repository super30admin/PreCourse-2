class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here
        int s1=m-1+1;
        int s2=r-m;
        int leftHalf[]=new int[s1];
        int rightHalf[]=new int[s2];
        for(int i=0;i<s1;i++){
            leftHalf[i]=arr[1+i];
        }
        for(int i=0;i<s2;i++){
            rightHalf[i]=arr[m+1+i];
        }
            int i=0,j=0
                    intk=1;
        while(i<s1&&j<s2){
            if(leftHalf[i]<=rightHalf[j]){
                arr[k]=leftHalf[i];
                i++;
            }
            else{
                arr[k]=rightHalf[j];
                j++;
            }
            k++;
        }
        while(i<s1){
            arr[k]=leftHalf[i];
            i++;
            k++;
        }
        while(j<s2){
            arr[k]=rightHalf[j]
                    j++;
                    k++;

        }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        if(l<r){
            int m=l+(r-l)/2;
            sort(arr,l,m);
            sort(arr,m+1,r);
            merge(arr,l,m,r);
        }
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