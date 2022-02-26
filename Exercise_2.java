/* Time Complexity : 
Best: O(n*log(n))
Worst: O(n^2) 

Space Complexity :no extra array used, O(1)
Did this code successfully run on Leetcode : yes
Any problem you faced while coding this : no

*/
class QuickSort 
{ 
    void swap(int arr[],int i,int j){
        int temp=arr[i];
        arr[i]=arr[j];
        arr[j]=temp;  
    }
    
    int partition(int arr[], int low, int high) 
    { 
   	    int pivot = arr[high];
        int k = low-1;

        for(int i=low;i<high;i++){
            if(arr[i]<pivot){
                k++;
                swap(arr,i,k);
            }
        }
        swap(arr,k+1,high);
        return k+1;  
    } 
    
    void sort(int arr[], int low, int high) 
    {  
           if(low<high){
            int pivot = partition(arr,low,high);
            sort(arr,low,pivot-1);
            sort(arr,pivot+1,high);
        } 
    } 
  
  
    static void printArray(int arr[]) 
    { 
        int n = arr.length; 
        for (int i=0; i<n; ++i) 
            System.out.print(arr[i]+" "); 
        System.out.println(); 
    } 
  
    // Driver program 
    public static void main(String args[]) 
    { 
        int arr[] = {10, 7, 8, 9, 1, 5}; 
        int n = arr.length; 
  
        QuickSort ob = new QuickSort(); 
        ob.sort(arr, 0, n-1); 
  
        System.out.println("sorted array"); 
        printArray(arr); 
    } 
} 
