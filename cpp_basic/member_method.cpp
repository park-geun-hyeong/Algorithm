//decomposition of member method's declaration & definition

#include<iostream>
using namespace std;

class Vec2{

public:
    Vec2();
    Vec2(float x, float y);

    float getx() const;
    float gety() const;

    static Vec2 Sum(Vec2 a, Vec2 b){
        return Vec2(a.x + b.x, a.y + b.y);
    }

    Vec2 Add(Vec2 rhs){
        return Vec2(x + rhs.x, y+rhs.y);
    }


private:
    float x;
    float y;
};

int main(){
    Vec2 a(2,3);
    Vec2 b(-1,4);
    Vec2 c1 = Vec2::Sum(a,b);
    Vec2 c2 = a.Add(b);


    cout<<a.getx()<<", "<<a.gety()<<endl;
    cout<<b.getx()<<", "<<b.gety()<<endl;
    cout<<c1.getx()<<", "<<c1.gety()<<endl;
    cout<<c2.getx()<<", "<<c2.gety()<<endl;



    return 0;
}

Vec2::Vec2() : x(0), y(0) {};
Vec2::Vec2(float x, float y): x(x),y(y) {};

float Vec2::getx() const {return x;}
float Vec2::gety() const {return y;}

