#include <iostream>
using namespace std;

int change_val(int &p){
    p = 3;
    return 0;
}

int& function(int& a){
    a=5;
    return a;
}

int main(){

    int number = 5;
    cout<<number<<endl;
    change_val(number);
    cout<<number<<endl;

    int x;
    int &y = x;
    int &z = y;

    x=1;
    cout<<x<<y<<z<<endl;

    y=2;
    cout<<x<<y<<z<<endl;

    z=3;
    cout<<x<<y<<z<<endl;

    int arr[3] = {1,2,3};
    int(&ref)[3] = arr;

    cout<<ref[0]<<ref[1]<<ref[2]<<endl;

    int b;
    int c = function(b);
    cout<<c<<endl;

}

