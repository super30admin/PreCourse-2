//Time Complexity: O(nlong)
//Space Complexity: O(n)
class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
       int p=m-l+1;
       int q=r-m;

       //Temp Arrays: 
       int left[]=new int[p];
       int right[]=new int[q];
       // copy data in temp arrays 
       for(int i=0;i<p;i++)
        { left[i]=arr[l+i];}
        
       for(int j=0;j<q;j++)
        { right[j]=arr[m+1+j];}

        //Merge the temp arrays back to array

        int i=0,j=0;
        int k=l;//initial index of merged subarray
        while (i<p && j<q) {
            if(left[i]<=right[j]){
                arr[k]=left[i];
                i++;
            }else{
                arr[k]=right[j];
                j++;
            }
            k++;
            
        }
        //copy remainig elements of left array
        while (i<p) {
            arr[k]=left[i];
            i++;
            k++;
            
        }
        //copy remaining elements of right array
        while (j<q) {
            arr[k]=right[j];
            j++;
            k++;
            
        }






    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here 

        if(l<r){
            int mid=l+(r-l)/2;
            sort(arr, l, mid);
            sort(arr, mid+1, r);
            //merge sorted halves
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