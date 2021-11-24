//Dynamic allocation
#include<iostream>
using namespace std;

int main(){

    int *a = new int(5);
    cout<<a<<endl;
    cout<<*a<<endl;

    *a = 10;
    cout<<a<<endl;
    cout<<*a<<endl;

    delete a; // free memory

    ///////////////////////////
    int *arr;
    int len;

    cout<< "input array length :"<<endl;
    cin>>len;

    arr = new int[len];

    for(int i=0; i<len; i++){
        arr[i] = len - i;
    }

    for(int i=0; i<len; i++){
        cout<< arr[i]<< " ";
    }

    delete[] arr;
    return 0;
}

