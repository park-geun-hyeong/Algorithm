#include<iostream>
using namespace std;

class Date{

private:
    int year_;
    int month_;
    int day_;

public:
    void SetDate(int year, int month ,int date){
        year_ = year;
        month_ = month;
        day_ = date;
    }

    void AddDay(int inc){
        day_ = day_ + inc;

        if(month_ == 1 || month_ == 3 || month_ == 5 || month_ == 7 || month_ == 8 || month_ == 10 || month_ == 12 ){
            if(day_ > 31){
                day_ = day_ - 31;
                month_ = month_ + 1;
                if(month_>12){
                    month_ = month_ - 12;
                    year_ = year_ + 1;
                }
            }
        }
        else if(month_ == 4 || month_ == 6 || month_ == 9 || month_ == 11){
            if(day_ > 30){
                day_ = day_ - 30;
                month_ = month_ + 1;
                    if(month_>12){
                    month_ = month_ - 12;
                    year_ = year_ + 1;
                }
            }
        }
        else{
            if(day_ > 28){
                day_ = day_ - 30;
                month_ = month_ + 1;
                if(month_>12){
                    month_ = month_ - 12;
                    year_ = year_ + 1;
                }
            }

        }
    }

    void AddMonth(int inc){
        month_ = month_ + 1;
        if(month_>12){
            month_ = month_ - 12;
            year_ = year_ + 1;
        }
    }

    void AddYear(int inc){
        year_ = year_ + 1;
    }


    void ShowDate(){
        cout<<"####### Date #######"<<endl;
        cout<< year_<<"-"<<month_<<"-"<<day_<<endl;
    }
};


int main(){

    Date date;
    date.SetDate(2022,6,25);
    date.AddDay(24);
    date.AddMonth(3);
    date.ShowDate();
    return 0;
}

