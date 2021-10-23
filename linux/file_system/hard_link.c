#include<unistd.h>
#include<stdio.h>
#include<stdlib.h>

// make hard link of file1 named file2

int main(int argc, char *argv[]){

	if(link(argv[1],argv[2]) == -1){
	
		exit(1);
	}
	exit(0);
	return 0;
}
