#include<stdlib.h> 
#include<stdio.h> 
  
// Merges two subarrays of arr[]. 
// First subarray is arr[l..m] 
// Second subarray is arr[m+1..r] 
void merge(int arr[], int l, int m, int r) 
{ 
    //Your code here
    int n1 = m-l+1;
    int n2 = r-m;
    
    int arrL[n1],arrR[n2];
    
    for(int i = 0;i<n1;i++){
    	arrL[i] = arr[l+i];
    }
    
    for(int j = 0;j<n2;j++){
    	arrR[j] = arr[m+j+1];
    }
    
    int i = 0;
    int j = 0;
    int k = l;
    while(n1>i&& n2> j){
    	
    	if(arrL[i]<arrR[j]){
    		arr[k] = arrL[i++];
    	} else {
    		arr[k] = arrR[j++];
    	}
    	k++;
    }
    
    while(n1>i){
    	
     	arr[k] = arrL[i++];
    	k++;
    }
    
    
    while(n2> j){
    	
      arr[k] = arrR[j++];
      k++;
    }
    
    
} 
  
/* l is for left index and r is right index of the 
   sub-array of arr to be sorted */
void mergeSort(int arr[], int l, int r) 
{ 
    //Your code here
    if ( l<r){
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