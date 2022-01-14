#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;


class Marine{
    static int total_marine_num; // disappear when program's ending

    int hp;
    int coord_x, coord_y;
    int damage;
    bool is_dead;


public:
    Marine();
    Marine(int x, int y);
    Marine(int x, int y, int default_damage);

    const int default_damage; //constant : default

    int attack();
    Marine& be_attacked(int damage_earn);
    void moving(int x, int y);

    void show_status();
    static void show_total_marine();
    ~Marine() {total_marine_num--;}

};
int Marine::total_marine_num = 0;

Marine::Marine() : hp(50), default_damage(5), coord_x(0), coord_y(0), is_dead(false) { total_marine_num++;}//initializer list
Marine::Marine(int x, int y) : hp(50), default_damage(5), coord_x(x), coord_y(y), is_dead(false) {total_marine_num++;}//initializer
Marine::Marine(int x, int y, int default_damage) : hp(50), default_damage(default_damage), coord_x(x), coord_y(y), is_dead(false) {total_marine_num++;}//initializer

int Marine::attack(){
    return default_damage;
}

Marine& Marine::be_attacked(int damage_earn){
    hp-= damage_earn;
    if(hp<=0){
        is_dead = true;
    }

    return *this;
}

void Marine::moving(int x, int y){
    coord_x += x;
    coord_y += y;
}

void Marine::show_status(){
    cout<< "Marine "<<endl;
    cout<<"Location: ("<<coord_x<<","<<coord_y<<")"<<endl;
    cout<<"HP: "<<hp<<endl;
    cout<<"Damage: "<<default_damage<<endl;

    printf("\n");
}

void Marine::show_total_marine(){
    cout<<"total Marine: "<<total_marine_num<<endl;
}

void create_marine(){
    Marine m3(10,10);
    m3.show_status();

    Marine::show_total_marine();
    printf("\n");
}

int main(){

    Marine m1(2,3,10);
    m1.show_status();
    //Marine::show_total_marine();


    Marine m2(3,4,15);
    m2.show_status();
    //Marine::show_total_marine();

    create_marine(); // local object of create_marine function

    m1.be_attacked(m2.attack()).be_attacked(m2.attack());
    m2.be_attacked(m1.attack());

    m1.show_status();
    m2.show_status();

    return 0;
}

