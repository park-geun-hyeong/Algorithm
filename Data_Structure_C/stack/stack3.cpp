#include<stack>
#include<iostream>

using namespace std;

int main(void){



    stack<int> st1;
    stack<int> st2;

    st1.push(1);
    st1.push(2);
    st1.push(3);

    st2.push(10);
    st2.push(20);
    st2.push(30);

    swap(st1, st2);

    while(!st1.empty()){

        cout<<st1.top()<<endl;
        st1.pop();

    }



    return 0;
}

