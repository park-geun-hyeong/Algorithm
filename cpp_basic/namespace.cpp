#include<iostream>

using namespace std;

int n;

void set();

namespace doodle{
    int n;
    void set();
}

namespace google{
    int n;
    void set();
}
namespace boo{
    int n;
    void set(){
        n = 55;
    }

    namespace goo{
        int n ;
        void set(){
            n = 66;
        }
    }
}

namespace gee{
    void set();
    namespace qee{
        void set();
        int n;
    }
    int n;
}

int main(){

    ::set();
    doodle::set();
    google::set();
    boo::set();
    boo::goo::set();
    gee::set();
    gee::qee::set();

    cout<<::n<<endl;
    cout<<doodle::n<<endl;
    cout<<google::n<<endl;
    cout<<boo::n<<endl;
    cout<<boo::goo::n<<endl;
    cout<<gee::n<<endl;
    cout<<gee::qee::n<<endl;
    return 0;
}

void set(){
    ::n=10;
}

void doodle::set(){
    doodle::n=20;
}
void google::set(){
    google::n=30;
}

void gee::set(){
    gee::n = 44;
}

void gee::qee::set(){
    qee::n = 99;
}

