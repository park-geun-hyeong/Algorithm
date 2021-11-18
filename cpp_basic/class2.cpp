#include<iostream>

using namespace std;

class Complex{

private:
    double real;
    double img;

public:
    Complex(){ // constructor(def __init__)
        real = 0 ;
        img = 0;
    }
    Complex(double real_, double img_){
        real = real_;
        img = img_;
    }

    double getreal(){
        return real;
    }

    void setreal(double real_){
        real = real_;
    }

    double getimg(){
        return img;
    }

    void setimg(double img_){
        img = img_;
    }
};


int main(){

    Complex c1;
    c1.setreal(1);
    c1.setimg(0.33);

    Complex c2 = Complex(2,3);
    Complex c3(2,3);
    Complex c4={4,5};


    cout<<"c1: "<< c1.getreal()<<", "<<c1.getimg()<<endl;
    cout<<"c2: "<< c2.getreal()<<", "<<c2.getimg()<<endl;
    cout<<"c3: "<< c3.getreal()<<", "<<c3.getimg()<<endl;
    cout<<"c4: "<< c4.getreal()<<", "<<c4.getimg()<<endl;

    return 0;
}

