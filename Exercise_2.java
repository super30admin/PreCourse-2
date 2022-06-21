//Time Complexity : O(nlogn)
//Space Complexity : O(nlogn)
class QuickSort 
{ 
    void swap(int arr[],int i,int j){
		int temp = arr[i];
		arr[i] = arr[j];
		arr[j] = temp;   
    }
    
    int partition(int arr[], int low, int high) 
    { 
		int pivot = arr[high];
		int i = low -1;
		
		for(int j = low; j <= high-1; j++) {
			
			if(arr[j] < pivot)
			{
				i++;
				swap(arr,i,j);
				
			}
		}
		
		swap(arr, i+1, high);
		return(i+1);
    } 

    void sort(int arr[], int low, int high) 
    {  
		if(low < high) {
			
			int p = partition(arr, low, high);
			sort(arr, low, p -1);
			sort(arr, p +1, high);
		}
    } 
  
    public static void printArray(int arr[]) 
    { 
        int n = arr.length; 
        for (int i=0; i<n; ++i) 
            System.out.print(arr[i]+" "); 
        System.out.println(); 
    } 
}

   class Main{
	   
	    // Driver program 
	    public static void main(String args[]) 
	    { 
	        int arr[] = {10, 7, 8, 9, 1, 5}; 
	        int n = arr.length; 
	  
	        QuickSort ob = new QuickSort(); 
	        ob.sort(arr, 0, n-1); 
	  
	        System.out.println("sorted array"); 
	        QuickSort.printArray(arr); 
	    } 
} 
