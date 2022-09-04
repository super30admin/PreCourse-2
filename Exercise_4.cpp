#include<stdlib.h> 
#include<stdio.h> 
  
// Merges two subarrays of arr[]. 
// First subarray is arr[l..m] 
// Second subarray is arr[m+1..r] 
void merge(int arr[], int l, int m, int r) 
{ 
	int size1 = m-l+1;
	int size2 = r -m;
	int a[size1];
	int b[size2];
	for(int i =0; i<size1;i++){
		a[i] = arr[l+i];
		}
		for(int i =0; i<size2;i++){
		b[i] = arr[m+1+i];
		}
		
		int i =0;
		int j= 0;
		int k=l;
		
		while(i<size1 && j<size2){
			if(a[i] < b[j]){
				arr[k] = a[i];
				k++;
				i++;
				}
				
				else{
					arr[k] = b[j];
					k++;
					j++;
					}
				}
					while(i<size1){
						arr[k] = a[i];
						k++;
						i++;
						}
						
					while(j<size2){
						arr[k] = b[j];
						k++;
						j++;
						}
			
		
    //Your code here
} 
  
/* l is for left index and r is right index of the 
   sub-array of arr to be sorted */
void mergeSort(int arr[], int l, int r) 
{ 
	if(l<r){
		int m = (l+r)/2;
		mergeSort( arr, l,m);
		mergeSort(arr,m+1,r);
		
		merge(arr,l,m,r);
		}
    //Your code here
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
