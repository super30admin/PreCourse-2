// Time Complexity : o(nlog(n)) 
// Space Complexity : o(n) 
class MergeSort 
{ 
   
    void merge(int arr[], int l, int m, int r) 
    {  
         int len1 = m-l+1;
        int len2 = r-m;

        int left[] = new int[len1];
        int right[] = new int[len2];

        for(int i=0;i<len1;i++)
            left[i] = arr[l+i];
        for(int i=0;i<len2;i++)
            right[i] = arr[(m+1)+i];

        int i = 0, j = 0;
        int k = l;
        while (i < len1 && j < len2) {
            if (left[i] <= right[j]) {
                arr[k] = left[i];
                i++;
            }
            else {
                arr[k] = right[j];
                j++;
            }
            k++;
        }

        while (i < len1) {
            arr[k] = left[i];
            i++;
            k++;
        }
        while (j < len2) {
            arr[k] = right[j];
            j++;
            k++;
        }
    } 
     { 
   
        if(l<r){
            int mid = l + ((r-l)/2);
            sort(arr,l,mid);
            sort(arr,mid+1,r);
            merge(arr,l,mid,r);    
        }
    } 

  
    static void printArray(int arr[]) 
    { 
        int n = arr.length; 
        for (int i=0; i<n; ++i) 
            System.out.print(arr[i] + " "); 
        System.out.println(); 
    } 
  
   
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