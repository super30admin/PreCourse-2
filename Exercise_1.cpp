//TC=O(log(n))
//SC=O(1)

#include<iostream>
using namespace std;
  
// A recursive binary search function. It returns 
// location of x in given array arr[l..r] is present, 
// otherwise -1 
int binarySearch(int arr[], int l, int r, int key){

    if(l>r){
        return -1;
    }
    else{
        int m=(l+r)/2;
        if(arr[m]==key){
            return m;
        }
        else if(arr[m]>key){
           return binarySearch(arr, l, m-1, key);
        }
        else{
           return binarySearch(arr, m+1, r, key);
        }
    }

}
  
int main(){
    int arr[] = { 2, 3, 4, 10, 40 }; 
    int n = sizeof(arr) / sizeof(arr[0]); 
    int x=4;
    int result=binarySearch(arr,0,n-1,x);
    if(result==-1){
        cout<<"Element not present"<<endl;
    }
    else{
        cout<<"Element is present at index "<<result<<endl;
    }
    return 0;
}