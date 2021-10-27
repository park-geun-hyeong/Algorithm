
#include<stdio.h>
#include<stdlib.h>
#include<string.h>



struct student{

    unsigned int id;
    char *name;
    int scores[3];
    double total;
    double ave;

};


int main(){


    int i;
    enum subject {KOR = 0, ENG, MATH};
    struct student score_table[4] = {{1001, "John",99,88,77},
                                       {1002, "Marry",100,90,95},
                                       {1003, "Steve",70,80,90},
                                       {1004, "Cook",60,61,62}};


    struct student *std;
    std = score_table;

    for(i =0; i<4; i++,std++){
        std->total = std->scores[KOR] + std->scores[ENG] + std->scores[MATH];
        std->ave = std->total / 3.0;
    }


    printf("ID      NAME      KOR    ENG   MATH      TOTAL      AVE\n");
    std=score_table;
    for(i =0; i<4; i++, std++){
        printf("%-6d %-7s %6d %6d %6d %10.2f %10.2f\n",std->id, std->name, std->scores[KOR], std->scores[ENG],std->scores[MATH], std->total, std->ave);

    }
    getchar();

    return 0;
}

