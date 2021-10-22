#include<sys/types.h>
#include<sys/stat.h>
#include<stdio.h>
#include<stdlib.h>


// using
// 1. compile: gcc -o fchmod fchmod.c
// 2. ./fchmod 777(any mode for test) test.txt(any file for test)

int main(int argc, char *argv[]){
	
	
	
	long strtol();
	int newmode;
	
	newmode = (int) strtol(argv[1], (char **) NULL, 8);
	if(chmod(argv[2], newmode) == -1){
	
		perror(argv[2]);
		exit(1);
	}
	
	exit(0);

	return 0;
}
