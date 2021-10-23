#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>


int main(int argc, char *argv[]){


	if(symlink(argv[1],argv[2])==-1){
		exit(1);
	}
	exit(0);
	return 0;

}
