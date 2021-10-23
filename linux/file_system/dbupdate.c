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
	if((fd=open(argv[1], O_RDWR)) == -1){
	
		perror(argv[1]);
		exit(2);
	}
	
	do {
	printf("\ninput number of student(update):");
	if(scanf("%d", &id) == 1){
		lseek(fd, (long)(id-START_ID)*sizeof(record), SEEK_SET);
		if((read(fd, (char*) &record, sizeof(record)) >0) && (record.id !=0)){
			printf("name:%s\t number:%d\t score:%d\n", record.name, record.id, record.score);
			printf("input new score:");
			scanf("%d", &record.score);
			lseek(fd, (long) -sizeof(record), SEEK_CUR); 
			write(fd, (char *) &record, sizeof(record));}
		else{
			printf("no %d record\n", id);
			}
				
	}
	else{
		printf("input error");
	} 
s
	printf("continue?(Y/N)");
	scanf("%c", &c);
		
	} while (c =='Y');
	close(fd);
	exit(0);
}
