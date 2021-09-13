//Binary Search 
public class Exercise_1{
    public static void main(String[] args) {
        int arr[]={1,4,6,9,12,14,16};
        int searchElement=12;
        int elementPosition=binarySearch(arr,0,arr.length,searchElement);
        if(elementPosition==-1) System.out.println("element not found");
        else System.out.println("element found at position "+elementPosition);
    }
    static int binarySearch(int arr[],int low,int high,int element){
        if(high>=low){
        int mid=((low+high)/2);
        if(arr[mid]==element) return mid+1;
        if(arr[mid]>element) return  binarySearch(arr,low,mid-1,element);
        else if(arr[mid]<element) return  binarySearch(arr,mid+1, high, element);
        }
        return -1;
    }
}