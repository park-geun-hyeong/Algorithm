#include<iostream>
#include<string.h>
using namespace std;

class Marine{

    int hp;
    int coord_x, coord_y;
    int damage;
    bool is_dead;
    char *name;


public:
    Marine();
    Marine(int x, int y, const char *marine_name);
    ~Marine(); //destructor: delete dynamic memory

    int attack();
    void be_attacked(int damage_earn);
    void moving(int x, int y);

    void show_status();
};


Marine::Marine(){

    hp = 50;
    coord_x = coord_y = 0;
    damage = 5;
    is_dead = false;
    name  = NULL;
}

Marine::Marine(int x, int y, const char *marine_name){

    name = new char[strlen(marine_name) +1];
    strcpy(name, marine_name);

    coord_x = x;
    coord_y = y;

    hp = 50;
    damage = 5;
    is_dead = false;
}

Marine::~Marine(){

    cout<< name << "'s destructor! "<<endl;
    if(name != NULL){
        delete[] name; // delete str
    }

}

int Marine::attack(){
    return damage;
}

void Marine::be_attacked(int damage_earn){
    hp -= damage_earn;
    if(hp<=0){
        is_dead = true;
    }
}

void Marine::moving(int x, int y){
    coord_x = x;
    coord_y = y;
}

void Marine::show_status(){
    cout<< "Marine: "<<name<<endl;
    cout<< "HP: "<<hp<<endl;
    cout<< "locations: ("<<coord_x<<","<<coord_y<<")"<<endl;
}

int main(){

    Marine *marines[100];

    marines[0] = new Marine(2,3, "Marine_1");
    marines[1] = new Marine(1,3, "Marine_2");

    marines[0] -> be_attacked(marines[1]->attack());
    marines[0] -> show_status();
    marines[1] -> show_status();

    delete marines[0];
    delete marines[1];

    return 0;
}

