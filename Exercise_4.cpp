#include<stdlib.h> 
#include<stdio.h> 
  
using  namespace std;


// Merges two subarrays of arr[]. 
// First subarray is arr[l..m] 
// Second subarray is arr[m+1..r] 
void merge(int arr[], int l, int m, int r) 
{ 
   const int n1=m-l+1;
   const int n2=r-m;
   int left[n1];
   int right[n2];
   for(int i=0;i<n1;i++)
   {
       left[i]=arr[i+l];
       
   }
   for(int j=0;j<n2;j++)
   {
       right[j]=arr[m+1+j];
   }
   int i=0;
   int j=0;
   int k=l;
   while(i<n1 && j<n2)
   {
       if(left[i]<=right[j])
       {
           arr[k]=left[i];
           i++;
           k++;
       }
       else
       {
           arr[k]=right[j];
           j++;
           k++;
       }
   }
   while(i<n1)
   {
       arr[k]=left[i];
       i++;
       k++;
   }
   while(j<n2)
   {
       arr[k]=right[j];
       j++;
       k++;
   }
} 

  
/* l is for left index and r is right index of the 
   sub-array of arr to be sorted */
void mergeSort(int arr[], int l, int r) 
{ 
    if(l>=r)
    {
        return;
    }
    int m = l +(r-l)/2;
    mergeSort(arr,l,m);
    mergeSort(arr,m+1,r);
    merge(arr,l,m,r);
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
