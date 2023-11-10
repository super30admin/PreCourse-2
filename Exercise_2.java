public class QuickSort 
{ 
    void swap(int arr[],int i,int j){
        int q = arr[i];
        arr[i] = arr[j];
        arr[j] = q;
    }
    
    int partition(int arr[], int low, int high) 
    { 
        int pivot = arr[high];
        int lp = low;
        int hp = high-1;
        while(lp<hp)
        {
        while(arr[lp]<=pivot && lp<hp)
        {
            lp++;
        }
        while(arr[hp]>=pivot && lp<hp)
        {
            hp--;
        }
        swap(arr, lp, hp);
        }
        swap(arr, lp, high);
        return lp;
    } 
    void sort(int arr[], int low, int high) 
    {  
        if (low >= high)
        {
         return;   
        }
        int lp = partition(arr, low, high);
        sort(arr, low, lp-1);
        sort(arr, lp+1, high);
    } 
    static void printArray(int arr[]) 
    { 
        int n = arr.length; 
        for (int i=0; i<n; i++) 
            System.out.print(arr[i]+" "); 
        System.out.println(); 
    } 
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
