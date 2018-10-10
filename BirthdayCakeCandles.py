#Birthday Cake Candles
#include<iostream>
using namespace std;
int findmax(int arr[],int n){
    int maximum=0;
    for(int i=0;i<n;i++){
        if(arr[i]>maximum)
           maximum=arr[i];
    }
return maximum;
}
int main()
{
    int n;
    cin>>n;
    int arr[n];
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }
    int maximum=findmax(arr,n);
    int count=0;
    for(int i=0;i<n;i++){
        if(arr[i]==maximum)
           count++;
    }
cout<<count;
return 0;
}
