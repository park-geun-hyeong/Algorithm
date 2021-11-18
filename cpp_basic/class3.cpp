#include<iostream>
using namespace std;

class Time{

public:
    Time(): h(0), m(0), s(0) {}

    Time(int s_): Time() {
        s=s_;
    }

    Time(int m_, int s_): Time(s_) {
        m = m_;
        s = s_;
    }

    Time(int h_, int m_, int s_): Time(m_, s_) {
        h = h_;
        m = m_;
        s = s_;
    }

    int gethour(){
        return h;
    }

    int getmin(){
        return m;
    }
    int getsec(){
        return s;
    }


private:
    int h;
    int m;
    int s;

};

int main(){

    Time c1;
    Time c2(15);
    Time c3(1, 23);
    Time c4(5, 12, 33);

    cout<<"time: "<<c1.gethour()<<":"<<c1.getmin()<<":"<<c1.getsec()<<endl;
    cout<<"time: "<<c2.gethour()<<":"<<c2.getmin()<<":"<<c2.getsec()<<endl;
    cout<<"time: "<<c3.gethour()<<":"<<c3.getmin()<<":"<<c3.getsec()<<endl;
    cout<<"time: "<<c4.gethour()<<":"<<c4.getmin()<<":"<<c4.getsec()<<endl;

    return 0;
}

