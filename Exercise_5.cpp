#include <bits/stdc++.h> 
using namespace std; 
  
// A utility function to swap two elements 
void swap(int* a, int* b) 
{ 
    int t = *a; 
    *a = *b; 
    *b = t; 
} 
  
/* This function is same in both iterative and recursive*/
int partition(int arr[], int l, int h) 
{ 
    //Do the comparison and swapping here 
    int t=h-1,it=h-1,x=arr[h];
    while(it>=l && t>=l){
        if(arr[it]>x){
            swap(&arr[it],&arr[t]);t--;
        }
        it--;
    }
    if(t==h){
        return t;
    }
    swap(arr[h],arr[t+1]);
    return (t+1);
} 
  
/* A[] --> Array to be sorted,  
l --> Starting index,  
h --> Ending index */
void quickSortIterative(int arr[], int l, int h) 
{ 
    //Try to think that how you can use stack here to remove recursion.
    stack<int> s;
    if(l==h){
        return;
    }
    int ll=l,hh=h;
    s.push(hh);s.push(ll);
    while(!s.empty() && ll<=hh){
        ll=s.top();s.pop();
        hh=s.top();s.pop();
        int p=partition(arr,ll,hh);
        //cout<<p<<' '<< arr[p] <<'\n';
        if((p+1)<=hh){
        s.push(hh);s.push(p+1);}
        if((p-1)>=ll){
        s.push(p-1);s.push(ll);}
    }
} 
  
// A utility function to print contents of arr 
void printArr(int arr[], int n) 
{ 
    int i; 
    for (i = 0; i < n; ++i) 
        cout << arr[i] << " "; 
} 
  
// Driver code 
int main() 
{ 
    int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 }; 
    int n = sizeof(arr) / sizeof(*arr); 
    quickSortIterative(arr, 0, n - 1); 
    printArr(arr, n); 
    return 0; 
} 