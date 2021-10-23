#include<stdio.h>
#include<stdlib.h>
#include<sys/stat.h>
#include<fcntl.h>
#include<unistd.h>


int main(int argc, char *argv[]){

	
	int fd;
	int close();
	if((fd = open(argv[1], O_RDWR)) == -1 ){
	
		printf("open error\n");
	}
	else 
		printf("open %s success: %d\n", argv[1], fd);
	
	close(fd);
	exit(0);


	return 0;
}
