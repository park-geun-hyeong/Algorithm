#include<iostream>
using namespace std;

//private, protected, public

struct tv{

private:
    bool powerOn;
    int channel;
    int volume;

public:
    void on(){
        powerOn=true;
        cout << "Turn on TV" <<endl;
    }

    void off(){
        powerOn = false;
        cout<<"Turn off TV"<<endl;
    }

    void setchannel(int ch){
        if(ch >= 0 && ch <=100){
            channel = ch;
            cout<< "channel: "<<channel<<endl;

        }
    }
    void setvolume(int vol){
        if(vol >= 0 && vol <=100){
            volume = vol;
            cout<<"volume: "<<volume<<endl;
        }
    }
};


int main(){

    tv lg;
    lg.on();
    lg.setchannel(20);
    lg.setvolume(30);
    lg.setvolume(-29);
    lg.off();

    return 0;
}

