#include<iostream>
#include<string.h>
using namespace std;

class String {
public:
    String(){
        cout<<"String()"<< endl;
        strData = NULL;
        len=0;
        }

    String(const char *str){
        cout<<"String(const char *str)"<<endl;
        len = strlen(str);
        strData = new char[len+1]; // last null(+1)
        cout<<"strData allocate: "<<(void*)strData<<endl;
        strcpy(strData, str); //deep copy
    }

    String(const String &rhs){
        cout<<"String(String &rhs) "<<endl;
        strData = new char[rhs.len + 1];
        cout<<"StrData allocate: "<<(void*)strData<<endl;
        strcpy(strData, rhs.strData);
        len = rhs.len;
    }

    ~String(){
        cout<<"~String()"<<endl;
        delete[] strData;
        cout <<"strData free: "<< (void*)strData<<endl;
        strData = NULL;
    }

    char *getstr() const { return strData; }
    int getlen() const{ return len;}


private:
    char *strData;
    int len;
};

int main(){

    String s1("hello");
    String s2(s1); // copy constructor(deep copy)

    cout<< s1.getstr()<<endl;
    cout<< s2.getstr()<<endl;

    return 0;

}

