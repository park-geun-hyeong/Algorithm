//decomposition of member method's declaration & definition

#include<iostream>
using namespace std;

class Vec2{

public:
    Vec2();
    Vec2(float x, float y);

    float getx() const;
    float gety() const;

    Vec2 operator+ (const Vec2 rhs) const;
    Vec2 operator- (const Vec2 rhs) const;
    Vec2 operator* (const float rhs) const;
    float operator* (const Vec2 rhs) const;
    Vec2 operator/ (const float rhs) const;

private:
    float x;
    float y;
};

Vec2 Sum(Vec2 a, Vec2 b);

int main(){
    Vec2 a(2,3);
    Vec2 b(-1,4);
    Vec2 c1 = Sum(a,b);
    Vec2 c2 = a.operator+(b);
    Vec2 c3 = a+b; //overloading
    Vec2 c4 = a-b;
    float c5 = a*b;
    Vec2 c6 = a * 2;
    Vec2 c7 = a / 2;


    cout<<a.getx()<<", "<<a.gety()<<endl;
    cout<<b.getx()<<", "<<b.gety()<<endl;
    cout<<c1.getx()<<", "<<c1.gety()<<endl;
    cout<<c2.getx()<<", "<<c2.gety()<<endl;
    cout<<c3.getx()<<", "<<c3.gety()<<endl;
    cout<<c4.getx()<<", "<<c4.gety()<<endl;
    cout<<c5<<endl;
    cout<<c6.getx()<<", "<<c6.gety()<<endl;
    cout<<c7.getx()<<", "<<c7.gety()<<endl;

    return 0;
}

Vec2::Vec2() : x(0), y(0) {};
Vec2::Vec2(float x, float y): x(x),y(y) {};

float Vec2::getx() const {return x;}
float Vec2::gety() const {return y;}

Vec2 Vec2::operator+(const Vec2 rhs) const{ // definite operator
        return Vec2(x + rhs.x, y+rhs.y);
    }

Vec2 Vec2::operator-(const Vec2 rhs) const{ // definite operator
        return Vec2(x - rhs.x, y-rhs.y);
    }

Vec2 Vec2::operator*(const float rhs) const{ // definite operator
        return Vec2(x * rhs, y*rhs);
    }

float Vec2::operator*(const Vec2 rhs) const{ // definite operator
        return float(x * rhs.x + y*rhs.y);
    }

Vec2 Vec2::operator/(const float rhs) const{ // definite operator
        return Vec2(x / rhs, y / rhs);
    }

Vec2 Sum(Vec2 a, Vec2 b) {
        return Vec2(a.getx() + b.getx(), a.gety() + b.gety());
    }

