#include<iostream>
using namespace std;

class Vec{

public:
    Vec(): x(0), y(0) {
        cout<<this<<": Vec()"<<endl;
    }

    Vec(const float x, const float y) : x(x), y(y) {
        cout << this << ": Vec(const float x, const float y)"<<endl;
    }

    ~Vec(){
        cout<< this<<": ~Vec()"<<endl;
    }

    float getx() const {return x;}
    float gety() const {return y;}

private:
    float x;
    float y;
};

int main(){

    Vec a;
    Vec b(1.0, 3.2);

    Vec *d1 = new Vec();
    Vec *d2 = new Vec(3,2);

    cout<< d1->getx()<< ", "<<d1->gety()<<endl;
    cout<< d2->getx()<< ", "<<d2->gety()<<endl;

    delete d1;
    delete d2;

    return 0;
}

