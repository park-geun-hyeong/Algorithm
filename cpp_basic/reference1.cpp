#include <iostream>
using namespace std;

int main(){

    int a = 3;
    int& another_a = a;

    another_a = 5;

    cout<< "a: "<<a<<endl;
    cout<<"another a: "<<another_a<<endl;


    return 0;
}

