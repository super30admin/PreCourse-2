#include<iostream> 
  
  using namespace std;
// Merges two subarrays of arr[]. 
// First subarray is arr[l..m] 
// Second subarray is arr[m+1..r] 
void merge(int arr[], int l, int m, int r) 
{ 
   

    //Your code here

    
     int res[r+1-l];
    int i=0;
    int j=0;
    int k=0;
    int size1= m+1-l;
    int size2= r-m;
    int size3=size1+size2;
    while(i<size1 && j<size2){
        if(arr[l+i]<arr[m+j+1]){

            res[k]=arr[l+i];

            i++;
            
        }
        else{ 
       
            res[k]=arr[m+j+1];
       
            j++;

        }
        k++;


    }

    while(i<size1){
     
               res[k]=arr[l+i];
               k++;
            i++;
        }

         while(j<size2){
     
         res[k]=arr[m+1+j];
         k++;
            j++;
        }

        for(int z=0;z<size1+size2;z++){
            arr[z+l]=res[z];
        }

        

} 
  
/* l is for left index and r is right index of the 
   sub-array of arr to be sorted */
void mergeSort(int arr[], int l, int r) 
{ 
    //Your code here
    if(l>=r){
        return;
    }
    int mid = l+(r-l)/2;
    mergeSort(arr,l,mid);
     mergeSort(arr,mid+1,r);
  
     merge(arr,l,mid,r);
} 
  
/* UTILITY FUNCTIONS */
/* Function to print an array */
void printArray(int A[], int size) 
{ 
    int i; 
    for (i=0; i < size; i++) 
        printf("%d ", A[i]); 
    printf("\n"); 
} 
  
/* Driver program to test above functions */
int main() 
{ 
   int arr[] = {12, 11, 13, 5, 6, 7}; 
    int arr_size = sizeof(arr)/sizeof(arr[0]); 
  
    printf("Given array is \n"); 
    printArray(arr, arr_size); 
  
    mergeSort(arr, 0, arr_size - 1); 
  
    printf("\nSorted array is \n"); 
    printArray(arr, arr_size); 
    return 0; 
}