#include<iostream>
using namespace std;

class Color{

public:
    Color() : r(0), g(0), b(0), id(idcnt++) {}
    Color(float r, float g , float b) : r(r), g(g), b(b), id(idcnt++) {}

    float getR(){ return r;}
    float getG(){ return g;}
    float getB(){ return b;}

    int getid(){ return id;}

    static Color MixColor(Color a, Color b){
        return Color((a.r + b.r)/ 2, (a.g + b.g)/ 2, (a.b + b.b)/ 2 ); // we can contact private
    }

    static int idcnt;

private:
    float r;
    float g;
    float b;

    int id;

};

int Color::idcnt = 1;

int main(){

    Color red(1,0,0);
    Color blue(0,0,1);

    Color purple = Color::MixColor(red, blue);

    cout<<"mix RGB"<<endl;
    cout<< "R: "<<purple.getR()<< " G: "<<purple.getG()<< " B: "<<purple.getB()<<endl;
    cout<< "red id: "<<red.getid()<<endl;
    cout<< "blue id: "<<blue.getid()<<endl;
    cout<< "purple id: "<<purple.getid()<<endl;

    return 0;
}

