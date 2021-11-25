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

    String &operator= (const String &rhs) {
        if (this != &rhs){
            delete[] strData;
            cout<<"String &operator(const String &rhs) "<<endl;
            strData = new char[rhs.len + 1];
            cout<<"StrData allocate: "<<(void*)strData<<endl;
            strcpy(strData, rhs.strData);
            len = rhs.len;

            return *this; // this: object's address, *this: object's content
        }
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
    char *strData; //pointer for dynamic allocated char type array
    int len;
};

int main(){

    String s1("hello");
    String s3;
    s3 = s1; // s3.operator=(s1)

    cout<< s1.getstr()<<endl;
    cout<< s3.getstr()<<endl;

    return 0;

}

