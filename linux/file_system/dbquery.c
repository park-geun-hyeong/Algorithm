#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<fcntl.h>
#include "student.h"


int main(int argc, char *argv[]){


	int fd, id;
	student record;
	int close();
	char c;
	
	
	if(argc<2){
	
		fprintf(stderr, "use: %s file\n ", argv[0]);
		exit(1);
	}
	if((fd=open(argv[1], O_RDONLY)) == -1){
	
		perror(argv[1]);
		exit(2);
	}
	
	do {
	printf("\ninput number of student:");
	if(scanf("%d", &id) == 1){
		lseek(fd, (id-START_ID)*sizeof(record), SEEK_SET);
		if((read(fd, (char*) &record, sizeof(record)) >0) && (record.id !=0)){
			printf("name:%s\t number:%d\t score:%d\n", record.name, record.id, record.score);}
		else{
			printf("no %d record\n", id);
			}
		
		
	}
	else{
		printf("input error");
	} 
		
	printf("continue?(Y/N)");
	scanf("%s", &c);
		
	} while (c =='Y');
	close(fd);
	exit(0);
}
