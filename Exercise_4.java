class Exercise_4 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  int k;
        int n1=m-l+1,n2=r-m;
        int le[]=new int[n1];
        int ri[]=new int[n2];
        for(int i=0;i<n1;i++)
            le[i]=arr[l+i];
        for(int j=0;j<n2;j++)
            ri[j]=arr[m+1+j];
        int j;
        int i;
        i=j=0;
        k=l;
        while(i<n1 && j<n2){
            if(le[i]<=ri[j])
                arr[k]=le[i++];
            else 
                arr[k]=ri[j++];
            k++;
          }

        while(i<n1)
            arr[k++]=le[i++];
        while(j<n2)
            arr[k++]=ri[j++];
        

       //Your code here  
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here
        if(l < r) {
            int mid = (l + r)/2;
            sort(arr, l, mid);
            sort(arr, mid + 1, r);
            merge(arr, l, mid, r);
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
    public static   void main(String args[]) 
    { 
        int arr[] = {12, 11, 13, 5, 6, 7}; 
  
        System.out.println("Given Array"); 
        printArray(arr); 
  
        Exercise_4 ob = new Exercise_4(); 
        ob.sort(arr, 0, arr.length-1); 
  
        System.out.println("\nSorted array"); 
        printArray(arr); 
    } 
} 