import java.util.Arrays;
class Quicksort {
	public static int partition(int a[],int low,int high) {
		int i=low;
		int j=low;
		int pivot=a[high];
		while(i<=high) {
			if(a[i]<=pivot) {
				int temp=a[i];
				a[i]=a[j];
				a[j]=temp;
				j++;
			}
			i++;
		}
		return j-1; 
	}
	
	public static void quickSort(int a[],int low,int high) {
		if(low<high) {
			int p=partition(a,low,high);
			//Recursion
			quickSort(a,low,p-1); //sorting for left
			quickSort(a,p+1,high);//sorting for right
			 
		}
		
	}
  public static void main(String args[]) {

    int[] data = { 8, 7, 2, 1, 0, 9, 6 };
    System.out.println("Unsorted Array");
    System.out.println(Arrays.toString(data));
    int size = data.length;
    Quicksort.quickSort(data, 0, size - 1);
    System.out.println("Sorted Array in Ascending Order ");
    System.out.println(Arrays.toString(data));
   
}}

