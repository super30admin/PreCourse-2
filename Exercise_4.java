//Time Complexity : O(nlogn)
//Space Complexity: O(n)

class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
        
        int n1 = m-l+1;
        int n2 = r-m;
       //Your code here  
        int merge1[] = new int[n1];
        int merge2[] = new int[n2];
        
        for(int i=0;i<n1;i++)
        {
            merge1[i] = arr[l+i];
        }
        
        for(int j=0;j<n2;j++)
        {
            merge2[j] = arr[m+1+j];
        }

        int i=0,j=0;
        
        int k=l;
        
        while(i<n1 && j<n2)
        {
            if(merge1[i] <= merge2[j])
            {
                arr[k] = merge1[i];
                i++;
            }
            else
            {
                arr[k] = merge2[j];
                j++;
            }
            
            k++;
        }
        
        while(i<n1)
        {
            arr[k] = merge1[i];
            i++;
            k++;
        }
        
        while(j<n2)
        {
            arr[k] = merge2[j];
            j++;
            k++;
        }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        if(r>l)
        {
            int center = (l+r)/2;
            
            sort(arr,l,center);
            sort(arr,center+1,r);
            
            //Call mergeSort from here 
            merge(arr,l,center,r);
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
  
        System.out.println("Given Array"); 
        printArray(arr); 
  
        MergeSort ob = new MergeSort(); 
        ob.sort(arr, 0, arr.length-1); 
  
        System.out.println("\nSorted array"); 
        printArray(arr); 
    } 
} 