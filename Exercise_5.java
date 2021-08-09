import java.util.Stack;

class IterativeQuickSort {
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable
        System.out.println(i+" "+j);
        arr[i]=arr[i]+arr[j];
        arr[j]=arr[i]-arr[j];
        arr[i]=arr[i]-arr[j];
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
        int p=h;
        while(l<h){
            while(l<arr.length&&arr[l]<arr[p])l++;
            while(h>=0&&arr[h]>=arr[p])h--;
            if(l<h){
                swap(arr,l,h);
            }
        }
        if (l<p)
        swap(arr,l,p);
        return l;

    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        Stack<int[]>stack=new Stack<>();
        if(l<h){
            stack.push(new int[]{l,h});
            while (!stack.isEmpty()){
                int a[]=stack.pop();
                int p=partition(arr,a[0],a[1]);
                if(p-1>a[0]){
                    stack.push(new int[]{a[0],p-1});
                }
                if(p+1<a[1]){
                    stack.push(new int[]{p+1,a[1]});
                }

            }
        }
    } 
  
    // A utility function to print contents of arr 
    void printArr(int arr[], int n) 
    { 
        int i; 
        for (i = 0; i < n; ++i) 
            System.out.print(arr[i] + " "); 
    } 
  
    // Driver code to test above 
    public static void main(String args[]) 
    { 
        IterativeQuickSort ob = new IterativeQuickSort(); 
        int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 }; 
        ob.QuickSort(arr, 0, arr.length - 1); 
        ob.printArr(arr, arr.length); 
    } 
} 