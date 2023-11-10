/*time complexity O(n^2)
 * Space complexity O(1)*/
class QuickSort 
{ 
    /* This function takes last element as pivot, 
       places the pivot element at its correct 
       position in sorted array, and places all 
       smaller (smaller than pivot) to left of 
       pivot and all greater elements to right 
       of pivot */
    void swap(int arr[],int i,int j){
        //Your code here   
    	int temp=0;
    	temp=arr[j];
    	arr[j]=arr[i];
    	arr[i]=temp;
    }
    
    int partition(int arr[], int low, int high) 
    { 
   	//Write code here for Partition and Swap 
   
    	int pivot=high;
    	int x=low;
     	int y=high-1;
    	while(true) {
     	while(true) {
    		if(arr[x]<=arr[pivot]&&x<=high-1) {
    			x++;
    		}
    		if(arr[y]>=arr[pivot]&&y>=low) {
    			y--;
    		}
    		if(x<y) {
    			break;
    		}
    		break;
    	}
    	if(x>y) {
    	swap(arr,pivot,x);
    	return x;
    	}
    	else {
    		swap(arr,x,y);
    	}
    	}
    	
    } 
    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    void sort(int arr[], int low, int high) 
    {  
    	if(low==high) {
    		return;
    	}
    	if(low>high) {
    		return;
    	}
       int i=partition(arr,low,high);     
       sort(arr,low,i-1);
       sort(arr,i+1,high);
    	// Recursively sort elements before 
            // partition and after partition 
    } 
  
    /* A utility function to print array of size n */
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
