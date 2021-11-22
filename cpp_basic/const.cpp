#include<iostream>
using namespace std;

// const: 데이터의 초기화가 이루어지면 그 값을 바꿀수 없도록 해주는 것

class Account{

public:
    Account(): money(0) {}
    Account(int money): money(money) {}

    void deposit(const int d){
        money += d;
        cout<<"deposit "<<d<<endl;
    }

    void draw(const int d){ //parameter const
        if(money>=d){
            money-=d;
            cout<<"draw "<<d<<endl;
        }
    }

    int viewmoney() const { // Member method const
        return money;
    }

private:
    int money;

};

int main(){

    Account park(100);

    cout<<"start money: "<<park.viewmoney()<<endl;
    park.deposit(20);
    park.draw(40);
    cout<<"remain money: "<<park.viewmoney()<<endl;


    return 0;
}

