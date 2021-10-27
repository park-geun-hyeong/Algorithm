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


    struct student *std[4];
    for(i=0;i<4;i++){
        std[i] = malloc(sizeof(struct student));
    }

    for(i =0; i<4; i++){

        std[i]->id = score_table[i].id;
        std[i]->name = score_table[i].name;
        std[i]->scores[KOR] = score_table[i].scores[KOR];
        std[i]->scores[ENG] = score_table[i].scores[ENG];
        std[i]->scores[MATH] = score_table[i].scores[MATH];

        std[i]->total = std[i]->scores[KOR] + std[i]->scores[ENG] + std[i]->scores[MATH];
        std[i]->ave = std[i]->total / 3.0;
    }


    printf("ID      NAME      KOR    ENG   MATH      TOTAL      AVE\n");
    for(i =0; i<4; i++){
        printf("%-6d %-7s %6d %6d %6d %10.2f %10.2f\n",std[i]->id, std[i]->name, (*std[i]).scores[KOR],(*std[i]).scores[ENG],(*std[i]).scores[MATH], (*std[i]).total, (*std[i]).ave);

    }
    getchar();

    return 0;
}

