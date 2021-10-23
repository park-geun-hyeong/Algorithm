#include<stdio.h>
#include<stdlib.h>
#include<fcntl.h>
#include<unistd.h>
#define BUFSIZE 512


int main(int argc, char *argv[]){

	char buffer[BUFSIZE];
	int fd;
	int close();
	ssize_t nread;
	long total = 0;
	
	
	if((fd = open(argv[1], O_RDONLY)) == -1){
		perror(argv[1]);
	}
	
	while((nread = read(fd, buffer, BUFSIZE)) > 0){
		total += nread;	
	}
	close(fd);
	printf("%s file size: %ld byte\n", argv[1], total);
	exit(0);
	
	return 0;

}
