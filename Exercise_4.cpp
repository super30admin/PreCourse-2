/***** timecomplexity O(nlogn)
 **********/
#include<stdlib.h> 
#include<stdio.h> 
  
// Merges two subarrays of arr[]. 
// First subarray is arr[l..m] 
// Second subarray is arr[m+1..r] 
void merge(int arr[], int l, int m, int r) 
{ 
    int sz1= m-l+1;
    int sz2= r-m;
    int arr1[sz1];
    int arr2[sz2];
    for(int i =0;i<sz1;i++)
    arr1[i]=arr[l+i];
    for(int i =0;i<sz2;i++)
    arr2[i]=arr[m+1+i];
    int i =0,j=0,k=l;
    while(i<sz1 &&j<sz2)
    {
       if(arr1[i]>arr2[j])
       {
        arr[k]=arr2[j];
        j++;
        k++;
       }
       else
       {
        arr[k]=arr1[i];
        i++;
        k++;
       }
    }
    while(i<sz1)
    {
     arr[k]=arr1[i];
     k++;
     i++;
    }
     while(j<sz2)
    {
     arr[k]=arr2[j];
     k++;
     j++;
    }

} 
  
/* l is for left index and r is right index of the 
   sub-array of arr to be sorted */
void mergeSort(int arr[], int l, int r) 
{  
    if(l<r)
    {
    int m = (l+r)/2;

    mergeSort(arr,l,m);
    mergeSort(arr,m+1,r);

    merge(arr,l,m,r);
    }
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